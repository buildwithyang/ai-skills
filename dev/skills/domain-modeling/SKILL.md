---
name: domain-modeling
description: "Domain Model discipline. 当用户需要校准 Ubiquitous Language 或 Bounded Context, 更新 CONTEXT.md, 或记录 ADR 时使用. 仅消费现有术语时不使用."
---

# Domain Modeling

## Purpose

对齐 requirements 背后的 domain meaning, boundaries 和 architecture decisions. `CONTEXT.md` 和 ADR 是 alignment artifacts, requirements 的 source of truth 仍是 Spec.

## Calibrate The Model

- 检查现有 `CONTEXT-MAP.md`, `CONTEXT.md`, ADR 和相关代码. 区分 current behavior, proposed model 和冲突.
- 将 ambiguous 或 overloaded term 收敛为 canonical term. 英文技术术语更准确时保留英文.
- 使用 concrete scenario 检查 Bounded Context, ownership, lifecycle, state transition 和 invariant.
- 发现模型与代码冲突时给出证据. 只询问会改变 boundary 或 decision 的问题.

## Maintain CONTEXT.md

确认 domain term 后, 按 [CONTEXT-FORMAT.md](./references/CONTEXT-FORMAT.md) 更新对应 `CONTEXT.md`.

- `CONTEXT.md` 只保存 Ubiquitous Language 和 domain definition.
- 文件按需创建.

## Record ADR

遇到 architecture decision 时读取 [ADR-FORMAT.md](./references/ADR-FORMAT.md). 只有满足全部 gate 才创建 ADR.

- ADR 只记录 decision 和 rationale, 不替代 Spec.
- Bounded Context decision 放在 context 内. System-wide decision 放在 repository root.

完成时报告已确认的 terms, boundary, docs changes 和 unresolved contradictions.
