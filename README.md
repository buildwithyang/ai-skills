# AI Skills

个人 AI skills 仓库，用一个目录维护可复用的 agent skills。

This is a personal AI skills repository for maintaining reusable agent skills in one place.

## Goals / 目标

中文：

* OpenClaw 是主要使用方。
* Codex 可以通过个人 agent skills 目录共用。
* Claude Code 只在需要调试时通过 `--add-dir` 临时加载。
* `skills/` 是唯一的 skill 源目录，避免多份拷贝漂移。

English:

* OpenClaw is the primary consumer.
* Codex can share the same skills through the personal agent skills directory.
* Claude Code loads these skills only when needed for debugging via `--add-dir`.
* `skills/` is the single source directory for skills to avoid duplicated copies drifting apart.

## Directory Structure / 目录结构

```text
.
├── AGENTS.md
├── README.md
├── .claude/
│   └── skills -> ../skills
└── skills/
    └── latest-news/
        ├── SKILL.md
        └── scripts/
            ├── fetch_rss.py
            └── news_api.py
```

中文：

* `skills/` 是唯一的 skill 源目录。
* `skills/<skill-name>/` 代表一个 skill。
* `.claude/skills` 是指向 `../skills` 的相对软链接，用于 Claude Code 临时调试。

English:

* `skills/` is the only source directory for skills.
* `skills/<skill-name>/` represents one skill.
* `.claude/skills` is a relative symlink to `../skills`, used for temporary Claude Code debugging.

## Skill Format / Skill 格式

推荐使用三方都容易识别的最小公共格式。

Use the smallest common format that all three tools can understand.

```text
skills/<skill-name>/
└── SKILL.md
```

Recommended `SKILL.md` format:

```markdown
---
name: skill-name
description: One-line description for when to use this skill.
---

Skill instructions...
```

中文：

* 为了兼容 OpenClaw，frontmatter 尽量保持简单。
* `name` 使用单行。
* `description` 使用单行。
* 共享 skill 不依赖 Claude-only 或 Codex-only 字段。

English:

* Keep frontmatter simple for OpenClaw compatibility.
* Use a single-line `name`.
* Use a single-line `description`.
* Shared skills should not depend on Claude-only or Codex-only fields.

## OpenClaw

OpenClaw 是这个仓库的主要使用方。

OpenClaw is the main consumer of this repository.

Recommended configuration:

```json
{
  "skills": {
    "load": {
      "extraDirs": [
        "/Users/yuhaiyang/Documents/code/myself/ai-skills/skills"
      ]
    }
  }
}
```

也可以通过个人 agent skills 目录加载。

You can also load the repository through the personal agent skills directory.

```bash
ln -s /Users/yuhaiyang/Documents/code/myself/ai-skills/skills ~/.agents/skills
```

如果 `~/.agents/skills` 已经存在，先检查里面是否有需要保留的 skills，不要直接覆盖。

If `~/.agents/skills` already exists, inspect it first and avoid overwriting existing skills.

## Codex

Codex 会读取个人 agent skills 目录：

Codex reads the personal agent skills directory:

```text
~/.agents/skills
```

如果已经为 OpenClaw 把 `~/.agents/skills` 指向本仓库的 `skills/`，Codex 可以共用同一批 skills。

If `~/.agents/skills` already points to this repository's `skills/` directory for OpenClaw, Codex can share the same skills.

## Claude Code

Claude Code 不作为主安装目标。需要临时调试本仓库 skills 时，使用 `--add-dir`：

Claude Code is not the primary installation target. Use `--add-dir` when you need to debug these skills temporarily:

```bash
claude --add-dir /Users/yuhaiyang/Documents/code/myself/ai-skills
```

Claude Code 会加载 added directory 里的：

Claude Code will load skills from:

```text
/Users/yuhaiyang/Documents/code/myself/ai-skills/.claude/skills
```

本仓库中的 `.claude/skills` 是相对软链接：

In this repository, `.claude/skills` is a relative symlink:

```text
.claude/skills -> ../skills
```

这样 Claude Code 可以读取同一批 `skills/`，但不会把 `~/.claude/skills` 指向本仓库，避免 Claude 安装 personal skill 时污染共享目录。

This lets Claude Code read the same `skills/` directory without pointing `~/.claude/skills` at this repository, avoiding accidental pollution when Claude installs personal skills.

## Add a New Skill / 新增 Skill

Create a skill directory:

```bash
mkdir -p skills/kubernetes
```

Create the entry file:

```bash
touch skills/kubernetes/SKILL.md
```

Final structure:

```text
skills/kubernetes/
└── SKILL.md
```

新增后：

* OpenClaw 通过 `extraDirs` 或 `~/.agents/skills` 加载。
* Codex 通过 `~/.agents/skills` 加载。
* Claude Code 调试时通过 `claude --add-dir /Users/yuhaiyang/Documents/code/myself/ai-skills` 加载。

After adding a skill:

* OpenClaw loads it through `extraDirs` or `~/.agents/skills`.
* Codex loads it through `~/.agents/skills`.
* Claude Code loads it for debugging through `claude --add-dir /Users/yuhaiyang/Documents/code/myself/ai-skills`.
