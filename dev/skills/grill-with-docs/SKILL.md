---
name: grill-with-docs
description: "组合 grilling 和 domain-modeling, 质询方案并规划 CONTEXT.md 和 ADR 更新."
disable-model-invocation: true
---

# Grill With Docs

1. 先调用 `grilling` 一次.
2. 如果 `grilling` 要求用户切换 Plan mode, 立即停止当前流程.
3. 已处于 Plan mode 时, 调用 `domain-modeling` 一次, 然后继续宿主的原生规划流程.
