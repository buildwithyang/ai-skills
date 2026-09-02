---
name: grill-me
description: "通过严格追问打磨已经初步成形的 product direction, plan 或 design."
disable-model-invocation: true
---

调用 `grilling` 一次.

## Next Skills

结束时输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$shape-idea`: product direction 仍不清晰.
- `$grill-with-docs`: 需要校准 Domain Model, `CONTEXT.md` 或 ADR.
- `$to-spec`: 方案已确认, 可以整理为 formal Spec.
