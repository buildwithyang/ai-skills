---
name: shape-idea
description: "通过初步 brainstorming 将模糊 product idea 澄清为已确认的 product direction, 然后交给 grill-me."
disable-model-invocation: true
---

# Shape Idea

对模糊 product idea 进行初步 brainstorming, 整理为用户能够解释和捍卫的 product direction. 只决定应该存在什么以及为什么, 不决定如何实现.

## Process

1. 用一句话重述当前 hypothesis, 包含 target user, problem 和 desired outcome. 对现有产品先检查可用的 high-level product context, 不向用户询问可以直接确认的事实.
2. 每轮只询问一个会明显改变 product direction 的决策, 直到 target user, problem, desired outcome, success evidence, constraints 和 non-goals 清晰. 提供 concrete choices, 并在有依据时给出 recommended answer.
3. 重要选择存在真实 trade-off 时, 给出 2-3 个 viable directions, 推荐项放在最前面. 说明 user-facing trade-off, 优先选择能够实现已确认 outcome 的最小方向, 不为常规细节制造 alternatives.
4. 输出 conversation 内的 Idea Brief, 请用户确认或修正. 未确认时继续澄清, 不进入 design.
5. 用户确认后完成 Idea Brief.

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

## Next Skills

结束时输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$grill-me`: 继续质询已确认的 product direction.
- `$grill-with-docs`: 后续代码库方案需要同步 Domain Model, `CONTEXT.md` 或 ADR.
