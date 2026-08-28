# ADR Format

只有以下 3 个 gate 全部成立时才创建 ADR:

1. 难以逆转.
2. 缺少 context 时令人意外.
3. 存在真实 trade-off.

- System-wide decision 放在 root `docs/adr/`.
- Bounded Context 内部 decision 放在该 context 的 `docs/adr/`.
- 文件使用递增编号和 kebab-case slug. 扫描最高编号后加 1.

## Template

```md
# {Short decision title}

{用 1 到 3 句话说明 context, decision 和 rationale.}
```

只有能增加 decision context 时才添加 optional sections: decision 会被重新审视时使用 `Status`, rejected alternatives 值得保留时使用 `Considered Options`, non-obvious downstream effects 需要说明时使用 `Consequences`.
