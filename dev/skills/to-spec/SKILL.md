---
name: to-spec
description: "将已确认的 conversation 或 decision-complete plan 整理为唯一一份 formal Spec. 不重新进行需求访谈."
disable-model-invocation: true
---

# To Spec

将当前 conversation, 已确认 plan 和 codebase facts 综合为唯一一份 formal Spec. 只做 synthesis, 不重新 grilling 用户.

## Preconditions

- 必须已有 confirmed requirements 或 decision-complete plan. 如果仍有会改变 scope, architecture 或 risk 的未决问题, 停止并建议先使用 `grill-me`. 需要同步 Domain Model 文档时改用 `grill-with-docs`.
- 优先读取 `docs/agents/delivery-workflow.md` 中的 Formal Spec section. 如果文件不存在, 再查找 repository 已有约定. 仍无法确认时, 只询问用户选择一个 destination, 并建议后续运行 `setup-dev-workflow` 持久化选择.
- 只维护一份 formal Spec. 不同时创建互相同步的 tracker Spec 和 local Spec.

## Process

1. 检查当前 codebase, project instructions 和相关实现, 区分 verified facts, confirmed decisions 和 assumptions.
2. 使用现有 `CONTEXT.md` vocabulary 并遵守相关 ADR. 如果需要改变 Domain Model 或 architecture decision, 停止并返回 `grill-with-docs` 或 `domain-modeling`.
3. 确认 testing seams 已经由前序 plan 决定. 优先选择能够验证 external behavior 的最高层且稳定的 testing seam. 只有 seam 选择会明显改变 architecture 或 verification cost 时才询问用户.
4. 使用下面的结构编写 Spec.
5. 没有 blocker 时, 将 Spec 发布到已确认的 source of truth, 然后返回 Spec location 和关键 assumptions.

## Spec Structure

### Problem Statement

从用户或系统角度描述需要解决的问题, 不提前描述实现.

### Desired Outcome

描述目标结果和可验证的 success evidence.

### Scope

分别列出 In Scope 和 Out of Scope.

### User Stories

只保留能澄清 actor, behavior 或 value 的 stories. 不为纯技术工作制造无意义的 user story.

### Requirements

使用稳定 ID, 例如 `REQ-001`. 每项 requirement 必须 observable, testable, 并说明正常行为和关键 failure behavior.

### Implementation Decisions

记录已经确认的 module boundaries, interfaces, API contracts, data model, migration strategy 和 operational constraints. 不写容易过期的具体 file paths 或完整 code snippets.

Prototype 产生的 state machine, schema 或 type shape 如果比 prose 更准确, 可以只保留表达 decision 所需的最小片段, 并标记来源.

### Testing Decisions

记录 testing seams, acceptance coverage, failure cases 和可复用的 existing test patterns. 测试 external behavior, 不绑定内部实现细节.

### Constraints And Assumptions

明确 permission, compatibility, performance, security, rollout 和 operational assumptions.

## Completion Gate

- Spec 中不存在隐藏的 product 或 architecture decision.
- Requirements 能被 `to-tickets` 拆分并追踪回稳定 ID.
- Spec 与 `CONTEXT.md`, ADR 和当前 codebase 不冲突.
- 用户可以明确确认这份 Spec 是后续实现的唯一 requirements source of truth.
