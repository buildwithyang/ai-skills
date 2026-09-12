---
name: to-spec
description: "将已确认的 conversation 或 plan 整理为按功能独立维护的产品 Spec. 不重新访谈或编写实现设计."
disable-model-invocation: true
---

# To Spec

将当前 conversation 和已确认 plan 综合为产品 Spec, 定义要解决的问题, 产品行为, 业务规则和验收条件. 代码仅用于核实上下文, 不把代码现状写进产品文档. 只做 synthesis, 不重新 grilling 用户.

## Preconditions

- 必须已有 confirmed requirements 或 decision-complete plan. 如果仍有会改变 scope, architecture 或 risk 的未决问题, 停止并建议先使用 `grill-me`. 需要同步 Domain Model 文档时改用 `grill-with-docs`.
- 优先读取 `docs/agents/delivery-workflow.md` 中的 Formal Spec section. 如果文件不存在, 再查找 repository 已有约定. 仍无法确认时, 只询问用户选择一个 destination, 并建议后续运行 `setup-dev-workflow` 持久化选择.
- 每个独立功能维护一份 formal Spec, 一个项目可以有多份. 不把新功能强行并入已有功能的 Spec, 也不为同一功能维护互相同步的 tracker / local 副本.

## Numbering

- 产品文档编号在项目内递增, 例如 `0001-account-workflow.md`, `0002-account-mailbox.md`.
- 每份 Spec 内部独立从 `REQ-001` 编号, 不接续其他 Spec 的 REQ 序号. 不同 Spec 可以同时拥有 `REQ-001`.
- 同一 Spec 后续修订保持已有 REQ ID 稳定. 跨文档引用使用 `Spec 0002 / REQ-001` 和链接, 不能仅用裸 REQ ID 判断归属.

## Process

1. 按需检查 project instructions 和相关实现, 核实已确认需求的上下文与依赖. 调查结果用于判断, 不记录技术栈清单, 代码快照或已实现 / 未实现状态.
2. 使用现有 `CONTEXT.md` vocabulary 并遵守相关 ADR. 如果需要改变 Domain Model 或 architecture decision, 停止并返回 `grill-with-docs` 或 `domain-modeling`.
3. 从已确认行为提取成功, 失败和边界场景, 定义可观察的验收结果.
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

按本文 Numbering 规则使用文档内稳定 ID. 每项 requirement 必须 observable, testable, 并说明正常行为和关键 failure behavior.

### Business Rules And Dependencies

按需记录业务不变量, 状态转换和对其他产品能力的依赖; 术语引用 CONTEXT.md, 跨功能规则引用所属 Spec. 简单功能无需重复 Requirements.

不设置 Implementation Decisions 或代码事实章节, 不记录技术栈, 模块调用关系, API / SQL / type shape, 数据库迁移, 库版本或当前测试实现. 必要的实现设计属于实施计划或 ADR, 本 skill 不另行生成这些文档. 用户明确要求的技术兼容性只写成可验收的产品约束.

### Acceptance Criteria

描述各角色可观察的成功结果, failure cases 和边界条件, 映射到本 Spec 的 REQ ID. 不记录测试工具, 现有 test patterns 或某次运行是否通过.

### Constraints And Assumptions

明确影响产品行为的 permission, compatibility, performance 和 security 约束及尚未验证的产品假设. 不混入部署步骤, 临时环境状态或调研过程记录.

## Completion Gate

- Spec 中不存在隐藏的 product decision 或实现方案, 不记录容易过期的代码现状.
- Requirements 能被 `to-tickets` 拆分并追踪回 `Spec + REQ ID`, 文档编号与文档内编号各自正确.
- Spec 与 `CONTEXT.md`, 相关 ADR 和已确认需求一致; 新需求与当前实现不同是正常情况, 不将当前实现当作产品约束.
- 用户可以明确确认这份 Spec 是该功能后续实现的唯一 requirements source of truth.

## Next Skills

结束时从以下选项中输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$to-tickets`: formal Spec 已确认, 可以拆分 delivery tickets.
- `$grill-me`: 仍有会改变 scope 或 requirements 的未决问题.
- `$grill-with-docs`: 仍需校准 Domain Model 或 architecture decisions.
- `$setup-dev-workflow`: Formal Spec 或 Issue provider configuration 尚未持久化.
