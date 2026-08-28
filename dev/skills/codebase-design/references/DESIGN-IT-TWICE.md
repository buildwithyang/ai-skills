# Design It Twice

只有已经选定 design candidate, 并且存在有意义的 Interface trade-off 时使用本流程.

## Process

1. 向用户说明 constraints, dependency categories 和必须保持的 behavior. 可以提供用于限定问题的 rough code sketch, 但不提前推荐方案.
2. 并行委派至少 3 个 sub-agents, 每个设计 radically different Interface:
   - 最小化 Interface, 目标是 1-3 个 entry points 和最大 Leverage.
   - 最大化 flexibility, 明确 extension cost.
   - 优化最常见 caller, 让 default path 最简单.
   - 存在 cross-seam dependency 时, 可增加 Ports and Adapters 方案.
3. 每个方案必须给出 Interface, caller example, hidden Implementation, dependency strategy 和 trade-offs.
4. 依次展示方案, 然后比较 Depth, Locality, Seam placement 和 operational consequences.
5. 给出明确 recommendation. 只有组合确实提高 Depth 或 Locality 时才提出 hybrid.

Sub-agent brief 必须包含 relevant file paths, coupling details, dependency category, 当前 project 的 Domain Model vocabulary, repository constraints 和 [CODE-DESIGN-STANDARDS.md](CODE-DESIGN-STANDARDS.md).
