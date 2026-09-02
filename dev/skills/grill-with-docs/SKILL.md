---
name: grill-with-docs
description: "组合 grilling 和 domain-modeling, 质询方案并规划 CONTEXT.md 和 ADR 更新."
disable-model-invocation: true
---

# Grill With Docs

1. 调用 `grilling` 质询方案并形成 decision-complete plan.
2. 调用 `domain-modeling` 校准 Domain Model, boundaries 和 architecture decisions, 并确定需要的 `CONTEXT.md` 和 ADR changes.
3. 将 Domain Model 结论和文档变更纳入 plan, 等待用户确认.

## Next Skills

结束时输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$domain-modeling`: 落盘已确认的 `CONTEXT.md` 或 ADR changes.
- `$to-spec`: Domain Model 文档已对齐, 可以整理 formal Spec.
