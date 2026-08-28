---
name: tdd
description: "Test-Driven Development. 当用户明确要求 test-first, Red-Green workflow, integration tests, 或另一个 Skill 明确调用时使用."
---

# Test-Driven Development

在已确认的 testing Seam 上使用 Red-Green vertical slices 实现 behavior. 每个 cycle 只增加一个 observable behavior, 测试通过 public Interface, 不绑定 internal structure.

## Preconditions

- 从 formal Spec, ticket 或用户明确说明的 behavior 开始. Source 提供 requirement ID 时保持 traceability.
- 优先使用前序 Spec 或 ticket 已确认的 testing Seam. 如果 Seam 缺失或失效, 仅就 Seam decision 向用户确认.
- 读取相关 `CONTEXT.md`, ADR 和 repository test conventions, 让 test vocabulary 与 Domain Model 一致.
- Interface shape 或 Seam placement 本身仍未决定时, 调用 `codebase-design` 后再写 test.

## Red-Green Cycle

1. 选择当前 requirement 中最小的 observable behavior slice.
2. **Red**: 通过 public Interface 写一个 behavior test. 运行 focused test, 确认它因目标 behavior 缺失而 Red.
3. **Green**: 只实现使当前 test 通过所需的最小 behavior. 不提前实现后续 slices 或 speculative extension.
4. 再次运行 focused test 和受影响的 nearby tests, 确认当前 slice green.
5. Source 提供 requirement ID 时记录对应关系, 然后选择下一个 slice 重复 cycle.

Red-Green cycle 不包含 refactor. 结构调整留给 `code-review`. Interface 或 Seam 需要改变时调用 `codebase-design`.

## Test Quality

- 需要替代 external dependency 或考虑 interaction assertion 时读取 [MOCKING.md](references/MOCKING.md).
- 优先验证 caller 可观察的 result, state transition, emitted event 或 error contract.

## Completion Gate

- 每个 In Scope requirement 都有通过已确认 Seam 的 behavior coverage.
- 每个新增 test 都观察到有意义的 Red, 然后通过对应的 Green implementation.
- Focused tests, affected tests 和 full relevant suite 均通过.
- Tests 不读取 private state, 不依赖 incidental call order, 并能承受 internal refactor.
- 返回 testing Seams, requirement coverage 和实际运行的 validation commands. 不自行 commit.
