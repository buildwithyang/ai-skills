# ADR Format

只有以下 3 个 gate 全部成立时才创建 ADR:

1. Hard to reverse.
2. Surprising without context.
3. Real trade-off.

- System-wide decision 放在 root `docs/adr/`.
- Bounded Context 内部 decision 放在该 context 的 `docs/adr/`.
- 文件使用 sequential number 和 kebab-case slug. 扫描最高编号后加 1.

## Template

```md
# {Short decision title}

{用 1 到 3 句话说明 context, decision 和 rationale.}
```

只有需要长期保留时才添加 `Status`, `Considered Options` 或 `Consequences`. ADR 保持 concise, 不替代 Spec.
