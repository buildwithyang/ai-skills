---
name: shape-idea
description: "将模糊的 product idea 澄清为已确认的 product direction, 不创建文件或设计 implementation."
disable-model-invocation: true
---

# Shape Idea

将一个模糊 product idea 整理为用户能够解释和捍卫的 product direction. 只决定应该存在什么以及为什么, 不决定如何实现.

## Process

1. 用一句话重述当前 hypothesis, 包含 target user, problem 和 desired outcome. 对现有产品只检查 high-level product context 和已确认事实, 不深入 implementation details.
2. 每轮只询问一个会明显改变 product direction 的决策, 直到 target user, problem, desired outcome, success evidence, constraints 和 non-goals 清晰. 提供 concrete choices, 并在有依据时给出 recommended answer.
3. 重要选择存在真实 trade-off 时, 给出 2-3 个 viable directions, 推荐项放在最前面. 优先选择能够实现已确认 outcome 的最小方向, 不为常规细节制造 alternatives.
4. 输出 conversation 内的 Idea Brief, 请用户确认或修正. 未确认时继续澄清, 不进入 design.
5. 用户确认后停止, 并提示用户在同一 conversation 中显式调用 `grill-with-docs`. 不代替用户调用下一个 Skill.

## Idea Brief

- Problem 和 target user.
- Desired outcome 和 success evidence.
- Chosen product direction.
- Constraints 和 non-goals.
- 3-7 个 core user stories, 使用 `As a <user>, I want <capability>, so that <outcome>.` 格式, 覆盖主要价值和重要 exceptions.

## Boundaries

- Idea Brief 只保留在当前 conversation, 不写入文件.
- 不创建 Spec, ADR, plan, ticket 或 implementation artifact.
- 不决定 architecture, API, schema, module, file 或 testing strategy.
- 如果 product direction 已经清晰, 直接总结并请求确认, 然后交给 `grill-with-docs`.

## Completion Gate

- Target user, problem 和 desired outcome 能用一句话表达.
- Success evidence, constraints 和 non-goals 明确.
- 每个 core user story 都支持 chosen direction.
- Idea Brief 不包含伪装成 product requirement 的 implementation decision.
- 用户已确认 Idea Brief, 当前 session 停在 `grill-with-docs` handoff 前.
