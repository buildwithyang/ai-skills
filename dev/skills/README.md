# Dev Skills

面向 Senior Developer 和 Software Architect 的软件开发, 调试, 测试和架构工作流.

每个 repository 首次使用时, 运行一次 `setup-dev-workflow`, 配置 Formal Spec, Epic, Issues 和 workflow labels.

默认 workflow:

`shape-idea -> grill-me -> to-spec -> to-tickets -> implement -> code-review`

每个 user-invoked workflow Skill 结束时输出当前适用的 1-3 个 `Next Skills`. 存在可用项时标记一个 Recommended, 没有时输出 `None`. Internal Skills 将结果返回 caller.

需要同步 Domain Model, `CONTEXT.md` 或 ADR 时, 使用 `grill-with-docs` 替代 `grill-me`. 两者不连续调用. `grill-with-docs` 方案确认后, 先显式调用 `domain-modeling` 落盘已确认的文档变更, 再调用 `to-spec`.

## Skills

- [shape-idea](./shape-idea/SKILL.md): 对模糊 product idea 进行初步 brainstorming, 然后交给 `grill-me`.
- [codebase-design](./codebase-design/SKILL.md): 使用 Deep Module vocabulary 设计 Interface 和 Seam, 并维护个人代码设计规范.
- [code-review](./code-review/SKILL.md): 从 Requirements 和 Engineering 两个独立 axis 审查 changes, 并按 severity 返回 findings.
- [domain-modeling](./domain-modeling/SKILL.md): 校准 Domain Model, Bounded Context 和 Ubiquitous Language, 并按需维护 `CONTEXT.md` 和 ADR.
- [grill-me](./grill-me/SKILL.md): 调用 `grilling`, 通过严格追问打磨已经初步成形的 product direction, plan 或 design.
- [grill-with-docs](./grill-with-docs/SKILL.md): 组合 `grilling` 和 `domain-modeling`, 对齐方案和 architecture decisions.
- [grilling](./grilling/SKILL.md): 质询关键方案决策并形成 decision-complete plan.
- [implement](./implement/SKILL.md): 根据 Spec 或 tickets 实现, review 并 commit.
- [setup-dev-workflow](./setup-dev-workflow/SKILL.md): 为 repository 配置 Formal Spec, Epic, Issues 和 workflow labels.
- [tdd](./tdd/SKILL.md): 在已确认的 testing Seam 上使用 Red-Green vertical slices 实现 behavior.
- [to-spec](./to-spec/SKILL.md): 将已确认方案整理为唯一一份 formal Spec, 作为后续实现的 requirements source of truth.
- [to-tickets](./to-tickets/SKILL.md): 将 formal Spec 拆分为可独立验证的 tracer-bullet ticket DAG.
