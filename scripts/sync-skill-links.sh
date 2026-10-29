#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "usage: $0 [--global]" >&2
  echo "  --global  also sync ~/.claude/skills and ~/.codex/skills" >&2
}

sync_global=false

for arg in "$@"; do
  case "$arg" in
    --global) sync_global=true ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage
      exit 1
      ;;
  esac
done

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
categories=(dev life productivity work)
skill_names=()
skill_sources=()

# Repo-local indexes use relative links, global indexes use absolute links.
destinations=("$repo_root/.agents/skills" "$repo_root/.claude/skills")
link_prefixes=("../.." "../..")

if [ "$sync_global" = true ]; then
  destinations+=("$HOME/.claude/skills" "$HOME/.codex/skills")
  link_prefixes+=("$repo_root" "$repo_root")
fi

for category in "${categories[@]}"; do
  category_dir="$repo_root/$category/skills"

  while IFS= read -r -d '' skill_file; do
    skill_dir="${skill_file%/SKILL.md}"
    skill_name="${skill_dir##*/}"

    for existing_name in "${skill_names[@]-}"; do
      if [ "$existing_name" = "$skill_name" ]; then
        echo "error: duplicate skill name: $skill_name" >&2
        exit 1
      fi
    done

    skill_names+=("$skill_name")
    skill_sources+=("${skill_dir#"$repo_root/"}")
  done < <(find "$category_dir" -mindepth 2 -maxdepth 2 -name SKILL.md -print0)
done

is_managed_link() {
  local link_target="$1"
  local prefix="$2"
  local category

  for category in "${categories[@]}"; do
    case "$link_target" in
      "$prefix/$category/skills/"*) return 0 ;;
    esac
  done

  return 1
}

for d in "${!destinations[@]}"; do
  destination="${destinations[$d]}"
  prefix="${link_prefixes[$d]}"
  mkdir -p "$destination"

  for i in "${!skill_names[@]}"; do
    skill_name="${skill_names[$i]}"
    relative_source="${skill_sources[$i]}"
    target="$destination/$skill_name"

    if [ -L "$target" ]; then
      if ! is_managed_link "$(readlink "$target")" "$prefix"; then
        echo "error: refusing to replace unmanaged symlink: $target" >&2
        exit 1
      fi
    elif [ -e "$target" ]; then
      echo "error: refusing to replace existing path: $target" >&2
      exit 1
    fi

    ln -sfn "$prefix/$relative_source" "$target"
    echo "linked $skill_name -> $relative_source ($destination)"
  done

  for target in "$destination"/*; do
    [ -L "$target" ] || continue

    if is_managed_link "$(readlink "$target")" "$prefix" && [ ! -e "$target/SKILL.md" ]; then
      rm "$target"
      echo "removed stale link: ${target##*/} ($destination)"
    fi
  done
done
