---
name: codebase-design
description: "Deep Module design discipline. 当用户明确要求设计或改进 Module Interface, 选择 Seam, 提高 testability, 或另一个 Skill 明确调用时使用."
---

# Codebase Design

设计 Deep Module: 用小而稳定的 Interface 隐藏大量 behavior, 将 Interface 放在清晰的 Seam, 并通过同一个 Interface 完成调用和测试. 目标是为 callers 提供 Leverage, 为 maintainers 提供 Locality.

## Vocabulary

使用以下精确术语. 不用 component, service, API 或 boundary 替代这些概念, 但保留 repository 已定义的 Domain term.

- **Module**: 同时具有 Interface 和 Implementation 的任意代码单元. 可以是 function, class, package 或 tier-spanning slice.
- **Interface**: caller 正确使用 Module 必须理解的完整 contract, 包括 type shape, invariants, ordering, error modes, configuration 和 performance characteristics.
- **Implementation**: Module 内部隐藏并实现其 behavior 的代码, 不等同于连接具体 dependency 的 Adapter.
- **Depth**: caller 学习一单位 Interface 后获得的 behavior leverage. 大量 behavior 隐藏在小 Interface 后面时, Module 是 deep 的.
- **Seam**: 无需修改 caller 即可替换 behavior 的位置. Seam placement 和 Interface design 是两个独立决策.
- **Port**: Module 拥有并定义的 Interface, 用于约束跨 architecture boundary 的 interaction.
- **Outbound Port**: Module 要求 external dependency 提供的 capabilities.
- **Adapter**: 在 Seam 将 concrete behavior 连接到 Port, 并封装具体 protocol, provider 或 infrastructure.
- **Leverage**: 一个小 Interface 为多个 callers 和 tests 提供的能力.
- **Locality**: change, bugs, knowledge 和 verification 集中在一个 Module 内, 而不是散落到 callers.

## Deep Module Principles

- 优先减少 Interface methods, parameters 和 caller-visible rules, 同时隐藏更多 complexity.
- Depth 由 Interface 提供的 Leverage 衡量, 不是 Implementation size 或 line count.
- 使用 deletion test. 删除 Module 后, 如果 complexity 会重新散落到多个 callers, 这个 Module 正在提供价值.
- Interface 同时是 caller surface 和 test surface. 测试必须穿过 Interface, 而不是绕过它验证 internals.
- 一个 Adapter 通常意味着 hypothetical Seam. 至少存在两个合理 Adapter, 例如 production 和 test Adapter 或 multiple providers 时, 才引入 Seam.
- Internal Seam 可以服务 Module 自身测试, 但不因为测试需要就暴露到 external Interface.

## Designing For Testability

- Dependencies 由 caller 显式提供, 不在 behavior 内部隐藏创建.
- Decision logic 优先返回 result, 由 orchestration layer 执行 side effects 和下一步 control flow.
- 选择能够验证 external behavior 的最高稳定 Seam.

## Personal Standards

设计, 实现, restructuring 或 review 代码时, 读取并应用 [CODE-DESIGN-STANDARDS.md](references/CODE-DESIGN-STANDARDS.md). 这是个人代码设计规范的唯一 source of truth. Repository 自己的 `AGENTS.md`, `CONTRIBUTING.md` 和 documented standards 仍然优先.

## Deeper Work

- 已经选定 shallow Module cluster, 需要根据 dependencies 调整 Seam 时, 读取 [DEEPENING.md](references/DEEPENING.md).
- 只有用户明确要求比较多个 Interface designs, 或前序 planning 已确认存在重大 Interface trade-off 时, 才读取并执行 [DESIGN-IT-TWICE.md](references/DESIGN-IT-TWICE.md).
