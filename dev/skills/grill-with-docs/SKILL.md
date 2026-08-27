---
name: grill-with-docs
description: "在原生 Plan mode 中组合 grilling 和 domain-modeling, 对齐 requirements, plan, domain meaning 和 architecture decisions."
disable-model-invocation: true
---

# Grill With Docs

分别调用 `grilling` 和 `domain-modeling`, 每个 Skill 单独调用一次.

- 先执行 `grilling` 的 Plan mode guard. 尚未进入 Plan mode 时停止并提示用户切换.
- 进入 Plan mode 后由 `grilling` 主导调查, 追问和 decision-complete plan.
- 同时由 `domain-modeling` 校准 terms, boundaries 和 architecture decisions, 并识别需要更新的 `CONTEXT.md` 或 ADR.
- Plan mode 中只把 document changes 写入 plan. 用户确认并进入可执行模式后, 再由 `domain-modeling` 更新文件.
- Spec 仍是 requirements 的 source of truth. 这个 Skill 不创建或替代正式 Spec.
