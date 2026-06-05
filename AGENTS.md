# AGENTS.md

## Goal

This repository is the single source of truth for reusable AI agent skills.

Supported agents:

* OpenClaw
* Codex
* Claude Code

Primary usage is OpenClaw. Codex can share the same skills through `~/.agents/skills`. Claude Code is used occasionally for debugging through `--add-dir`.

## Repository Structure

```text
.
├── AGENTS.md
├── README.md
├── .claude/
│   └── skills -> ../skills
└── skills/
    └── <skill-name>/
        └── SKILL.md
```

`skills/` is the only source directory for reusable skills. Each direct child directory under `skills/` is one skill.

## Compatibility

Use the smallest common skill format unless a skill is explicitly tool-specific:

```markdown
---
name: skill-name
description: One-line description for when to use this skill.
---

Instructions...
```

Keep YAML frontmatter simple for OpenClaw compatibility:

* Use single-line `name`.
* Use single-line `description`.
* Avoid Claude-only or Codex-only fields in shared skills.

## Creating Skills

Create a new skill only when:

* The knowledge is reusable.
* The problem occurs repeatedly.
* The instructions are specific enough to improve agent behavior.

Create new shared skills under:

```text
skills/<skill-name>/SKILL.md
```

Do not install Claude Code personal skills into this repository unless they are intended to be shared with OpenClaw and Codex.
