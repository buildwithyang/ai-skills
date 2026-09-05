---
name: domain-modeling
description: "Domain Model discipline. 当用户需要校准 Ubiquitous Language 或 Bounded Context, 更新 CONTEXT.md, 或记录 ADR 时使用. 仅消费现有术语时不使用."
---

# Domain Modeling

## Purpose

对齐 requirements 背后的业务含义, boundaries 和 architecture decisions. `CONTEXT.md` 记录 Bounded Context 的职责和业务术语. ADR 记录重要 architecture decision 及其原因和取舍. Requirements 的 source of truth 仍是 Spec.

## Align The Domain Model

- 检查现有 `CONTEXT-MAP.md`, `CONTEXT.md`, ADR 和相关代码. 说明 current behavior 是什么, proposed model 准备改变什么, 以及两者的差异.
- 同一概念有多个名称, 或同一名称表示多个概念时, 选择一个 canonical term. 英文技术术语更准确时保留英文.
- 使用具体业务场景检查 Bounded Context, ownership, lifecycle, state transition 和 invariant 是否合理, 即谁负责什么, 对象如何变化, 哪些业务规则必须始终成立.
- 发现 Domain Model 与代码行为不一致时给出证据. 只询问会改变 boundary 或 architecture decision 的问题.

## Maintain CONTEXT.md

确认 domain term 后, 按 [CONTEXT-FORMAT.md](./references/CONTEXT-FORMAT.md) 更新对应 `CONTEXT.md`.

- `CONTEXT.md` 只保存 Ubiquitous Language 和 domain definition.
- 文件按需创建.

## Record ADR

遇到 architecture decision 时读取 [ADR-FORMAT.md](./references/ADR-FORMAT.md). 只有满足全部 gate 才创建 ADR.

- ADR 只记录 decision 和 rationale, 不替代 Spec.
- Bounded Context decision 放在 context 内. System-wide decision 放在 repository root.

完成时报告已确认的 terms, boundary, docs changes 和 unresolved contradictions.
