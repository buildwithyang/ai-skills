#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
categories=(dev life work)
destinations=("$repo_root/.agents/skills" "$repo_root/.claude/skills")
skill_names=()
skill_sources=()

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

for destination in "${destinations[@]}"; do
  mkdir -p "$destination"

  for i in "${!skill_names[@]}"; do
    skill_name="${skill_names[$i]}"
    relative_source="${skill_sources[$i]}"
    target="$destination/$skill_name"

    if [ -L "$target" ]; then
      existing_target="$(readlink "$target")"
      case "$existing_target" in
        ../../dev/skills/*|../../life/skills/*|../../work/skills/*) ;;
        *)
          echo "error: refusing to replace unmanaged symlink: $target" >&2
          exit 1
          ;;
      esac
    elif [ -e "$target" ]; then
      echo "error: refusing to replace existing path: $target" >&2
      exit 1
    fi

    ln -sfn "../../$relative_source" "$target"
    echo "linked $skill_name -> $relative_source ($destination)"
  done

  for target in "$destination"/*; do
    [ -L "$target" ] || continue
    existing_target="$(readlink "$target")"

    case "$existing_target" in
      ../../dev/skills/*|../../life/skills/*|../../work/skills/*)
        if [ ! -e "$target/SKILL.md" ]; then
          rm "$target"
          echo "removed stale link: ${target##*/} ($destination)"
        fi
        ;;
    esac
  done
done
