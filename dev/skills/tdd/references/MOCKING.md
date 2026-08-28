# Mocking And Test Doubles

Test double 用于替代无法在当前 test scope 内可靠运行的 dependency, 不用于复制 owned internal structure.

## Decision Order

1. Pure computation 或 in-memory state 直接使用真实 Implementation.
2. 存在可靠 local stand-in 时优先使用 stand-in, 例如 temporary filesystem 或 embedded database.
3. Remote but owned service 使用 domain-oriented port. Tests 使用 in-memory Adapter, production 使用 network Adapter.
4. True external service 使用 injected port 和 fake, stub 或 mock Adapter.

## Mock At Real Boundaries

适合 test double 的 boundaries:

- Third-party API.
- Time 和 randomness.
- Filesystem 或 database 无法使用可靠 local stand-in 时.
- Network transport.

优先使用真实 owned Module. 不 mock private methods 或只为测试创建的 pass-through abstraction.

## Interaction Assertions

默认断言 observable outcome, 不断言内部调用次数或顺序.

只有 interaction 本身属于 contract 时才验证 interaction, 例如 exactly-once delivery, audit emission 或禁止重复 charge. 即使如此, assertion 也应该对应明确 requirement.

## Adapter Coverage

In-memory Adapter 验证 Domain behavior, 不能证明 network protocol 正确.

为 production Adapter 增加 contract 或 integration tests, 覆盖 serialization, authentication, timeout, retry, error mapping 和 compatibility. 不在每个 Domain test 中重复 transport coverage.
