---
name: code-review
description: "审查代码变更是否符合已确认需求和项目约定. 当用户要求 code review, 或另一个 Skill 明确调用时使用."
---

# Code Review

在 `implement` 完成实现后, 或用户单独要求时, 审查需求覆盖和实现质量.

## Workflow

1. 沿用用户或调用方指定的范围. `implement` 调用时, 覆盖本次任务的 staged, unstaged 和相关 untracked files, 排除无关变更.
2. 从关联 Spec, ticket 和用户已确认的方案或修订获取需求. 需要定位 Spec 或 Issue 时, 读取 `docs/agents/delivery-workflow.md` 中的配置. 缺少可信需求来源时, 说明需求覆盖未评估, 继续审查实现质量.
3. 按项目约定, `CONTEXT.md` 和 ADR 审查实现, 并应用 [CODE-DESIGN-STANDARDS.md](../codebase-design/references/CODE-DESIGN-STANDARDS.md). 项目约定优先于个人规范. 涉及 Module design 时调用 `codebase-design`.

## Review

- **Requirements**: 本次范围内的需求和 acceptance criteria 是否完整实现. Spec 提供 requirement ID 时, 用它关联问题和验证证据.
- **Engineering**: 实现质量是否满足项目约定, Interface contract 和已确认的 architecture decisions.

分别说明这两方面的结论. 优先报告影响交付的问题, 标明位置, 影响, 依据和修正建议, 并说明未完成的验证.

## Handoff

将问题和必要的 refactor 建议返回用户或调用方. `code-review` 只负责审查, `implement` 负责当前范围内的修复, 验证和后续 commit.

需要改变 Interface 或 Seam 时, 由 `codebase-design` 先完成设计. 新增需求或 architecture decision 交回规划流程确认.
