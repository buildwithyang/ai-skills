# AI Skills

个人 AI Skill 仓库. Skill 按用途分类存储, 同时通过扁平兼容索引供 Codex, Claude Code 和其他兼容 Agent Skills 的工具加载.

## Directory Layout

```text
.
|-- dev/
|   `-- skills/                 Development skills
|       |-- code-review/
|       |-- codebase-design/
|       |-- domain-modeling/
|       |-- grill-me/
|       |-- grill-with-docs/
|       |-- grilling/
|       |-- implement/
|       |-- setup-dev-workflow/
|       |-- shape-idea/
|       |-- tdd/
|       |-- to-spec/
|       `-- to-tickets/
|-- life/
|   `-- skills/                 Personal and daily-life skills
|       `-- latest-news/
|-- work/
|   `-- skills/                 Work and domain skills
|-- .agents/
|   `-- skills/                 Codex discovery index
|       |-- code-review -> ../../dev/skills/code-review
|       |-- codebase-design -> ../../dev/skills/codebase-design
|       |-- domain-modeling -> ../../dev/skills/domain-modeling
|       |-- grill-me -> ../../dev/skills/grill-me
|       |-- grill-with-docs -> ../../dev/skills/grill-with-docs
|       |-- grilling -> ../../dev/skills/grilling
|       |-- implement -> ../../dev/skills/implement
|       |-- latest-news -> ../../life/skills/latest-news
|       |-- setup-dev-workflow -> ../../dev/skills/setup-dev-workflow
|       |-- shape-idea -> ../../dev/skills/shape-idea
|       |-- tdd -> ../../dev/skills/tdd
|       |-- to-spec -> ../../dev/skills/to-spec
|       `-- to-tickets -> ../../dev/skills/to-tickets
|-- .claude/
|   `-- skills/                 Claude Code discovery index
|       |-- code-review -> ../../dev/skills/code-review
|       |-- codebase-design -> ../../dev/skills/codebase-design
|       |-- domain-modeling -> ../../dev/skills/domain-modeling
|       |-- grill-me -> ../../dev/skills/grill-me
|       |-- grill-with-docs -> ../../dev/skills/grill-with-docs
|       |-- grilling -> ../../dev/skills/grilling
|       |-- implement -> ../../dev/skills/implement
|       |-- latest-news -> ../../life/skills/latest-news
|       |-- setup-dev-workflow -> ../../dev/skills/setup-dev-workflow
|       |-- shape-idea -> ../../dev/skills/shape-idea
|       |-- tdd -> ../../dev/skills/tdd
|       |-- to-spec -> ../../dev/skills/to-spec
|       `-- to-tickets -> ../../dev/skills/to-tickets
|-- LICENSES/
|   `-- mattpocock-skills-MIT.txt
`-- scripts/
    `-- sync-skill-links.sh
```

## Source Of Truth

真实 Skill 源码只存放在以下分类目录:

- `dev/skills/<skill-name>/`
- `life/skills/<skill-name>/`
- `work/skills/<skill-name>/`

`.agents/skills/` 和 `.claude/skills/` 是由软链接组成的发现索引. 它们不是 Skill 源码目录.

当前 Skill 的真实位置:

- `code-review`: `dev/skills/code-review/`
- `codebase-design`: `dev/skills/codebase-design/`
- `domain-modeling`: `dev/skills/domain-modeling/`
- `grill-me`: `dev/skills/grill-me/`
- `grill-with-docs`: `dev/skills/grill-with-docs/`
- `grilling`: `dev/skills/grilling/`
- `implement`: `dev/skills/implement/`
- `latest-news`: `life/skills/latest-news/`
- `setup-dev-workflow`: `dev/skills/setup-dev-workflow/`
- `shape-idea`: `dev/skills/shape-idea/`
- `tdd`: `dev/skills/tdd/`
- `to-spec`: `dev/skills/to-spec/`
- `to-tickets`: `dev/skills/to-tickets/`

## Agent Compatibility

- Codex 通过 `.agents/skills/` 发现 Skill.
- Claude Code 通过 `.claude/skills/` 发现 Skill.

所有入口最终指向同一份分类源码, 不需要复制 Skill 内容.

## Add A Skill

先在合适的分类目录创建 Skill. 例如开发类 Skill:

```bash
mkdir -p dev/skills/my-skill
```

创建 `dev/skills/my-skill/SKILL.md`:

```markdown
---
name: my-skill
description: Explain when this skill should be used.
---

Skill instructions.
```

然后更新扁平兼容索引:

```bash
./scripts/sync-skill-links.sh
```

新增, 移动或删除 Skill 后都需要运行该脚本.

## Constraints

- 不要直接在 `.agents/skills/` 或 `.claude/skills/` 下创建真实 Skill 目录.
- 不同分类中的 Skill 名称必须全局唯一.
- 同步脚本遇到重复名称或现有非托管路径时会停止, 不会直接覆盖.
- Shared Skill 使用标准的 `SKILL.md` 格式, Agent 专属配置放在 Skill 自己的可选目录中.

## Upstream Sources

- `dev/skills/code-review/`, `dev/skills/codebase-design/`, `dev/skills/grilling/`, `dev/skills/grill-me/`, `dev/skills/domain-modeling/`, `dev/skills/grill-with-docs/`, `dev/skills/implement/`, `dev/skills/setup-dev-workflow/`, `dev/skills/tdd/`, `dev/skills/to-spec/` 和 `dev/skills/to-tickets/` 基于 [mattpocock/skills](https://github.com/mattpocock/skills) 定制.
- `dev/skills/shape-idea/` 从较早的个人 [buildwithyang/skills](https://github.com/buildwithyang/skills) revision `cc7b8f9c99fd531bd70353277da98e958812b251` 迁移并定制.
- 上游版本和 MIT 许可证保存在 [`LICENSES/mattpocock-skills-MIT.txt`](./LICENSES/mattpocock-skills-MIT.txt).
