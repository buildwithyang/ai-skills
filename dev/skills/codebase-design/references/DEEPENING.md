# Deepening

在深化 shallow Module cluster 前, 先分类它的 dependencies. Dependency category 决定 Seam placement 和 testing strategy.

## Dependency Categories

### In-Process

Pure computation 或 in-memory state. 可以合并 Module, 并直接通过新的 Interface 测试. 通常不需要 Adapter.

### Local-Substitutable

存在可在 local test 中运行的替代实现, 即 stand-in, 例如 in-memory filesystem 或 embedded database. Deep Module 可以在测试中使用 stand-in, 不需要把 internal Seam 暴露到 external Interface.

### Remote But Owned

跨 network boundary 的内部 service. 在 Seam 定义 Outbound Port, production 使用 network Adapter, tests 使用 in-memory Adapter. Domain behavior 仍留在 Deep Module 内.

### True External

无法控制的 third-party service. 将 external dependency 作为 injected Outbound Port, tests 使用 mock or fake Adapter.

## Seam Discipline

- Internal Seam 和 external Seam 分开. 不把 test-only variation 扩散给 callers.
- Deepening 应减少 caller-visible complexity, 而不是在旧 Module 外再增加一层 delegation.

## Testing Strategy

- 新 tests 通过 deepened Module Interface 验证 observable behavior.
- 新 Interface tests 覆盖旧 behavior 后, 删除只绑定 shallow internals 的重复 tests.
- Internal refactor 不应该迫使 Interface behavior tests 改写.
