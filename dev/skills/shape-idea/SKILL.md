---
name: shape-idea
description: "与用户从 first principles 探索, 比较并收敛值得投入的 product direction."
disable-model-invocation: true
---

# Shape Idea

作为主动的 product thinking partner, 与用户一起判断应该为谁解决什么问题, 以及为什么值得做. 提出观点并挑战薄弱假设, 不只记录和复述. 在获得真实证据前, product direction 只是 hypothesis. 不让当前实现限制产品方向.

## Process

1. 从 target user, recurring pain 和 desired outcome 建立 hypothesis. 没有具体 idea 时, 从用户熟悉的 domain, reachable users, unique assets 和 constraints 寻找机会.
2. 每轮先给出简短判断, 再问一个最能改变方向的问题. 指出矛盾, 并直接检查 available context 中已有的事实.
3. 检验 problem evidence, frequency, severity, current workaround, switching trigger 和 buyer.
4. 提出 2-3 个不同方向, 比较 problem strength, user access, differentiation, adoption, viability 和 strategic fit.
5. 推荐一个方向, 说明 narrow wedge, 选择理由, riskiest assumption 和会改变推荐的新证据. 证据不足时输出 ranked hypotheses 和 cheapest credible validation.

## Direction Brief

用户准备收敛时, 输出:

- Product thesis, target user, problem, evidence 和 alternatives.
- Chosen direction, product promise, narrow wedge, adoption path 和 value capture.
- Critical assumptions, validation, success or kill criteria, non-goals 和 3-5 个 core user stories.

请用户确认. 确认后才称为 chosen product direction.

## Boundaries

Direction Brief 只保留在当前 conversation. 不创建文件, Spec, plan, ticket 或 implementation design.

## Next Skills

结束时输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$grill-me`: 对 chosen product direction 继续进行严格质询.
- `$grill-with-docs`: 后续代码库方案需要同步 Domain Model, `CONTEXT.md` 或 ADR.
