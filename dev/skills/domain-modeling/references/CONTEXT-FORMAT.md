# CONTEXT.md Format

`CONTEXT.md` 只保存 Bounded Context 的 Ubiquitous Language.

```md
# {Context Name}

{用 1 到 2 句话说明这个 Bounded Context 的职责.}

## Ubiquitous Language

**Order**:
{用 1 到 2 句话定义这个 domain concept.}
_Avoid_: Purchase, Transaction
```

- 每个 concept 只选择一个 canonical term. 用 `_Avoid_` 记录 ambiguous synonyms.
- 只记录当前业务 domain 特有的 concept. 排除 implementation detail, requirement, plan 和 architecture decision.
- 如果存在 `CONTEXT-MAP.md`, 使用它定位 context. 否则使用 root `CONTEXT.md`.
- 未确认的 proposal 和 question 不写入 glossary.
