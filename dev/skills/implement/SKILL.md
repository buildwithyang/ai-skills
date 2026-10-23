---
name: implement
description: "根据 Spec 或 tickets 实现工作."
disable-model-invocation: true
---

实现用户在 Spec 或 tickets 中描述的工作.

根据 ticket 选择实现工作时, 按 `docs/agents/delivery-workflow.md` 的 label mapping 识别 state role, 排除 `deferred` 及存在未解除 blocker 的 tickets. 用户明确要求恢复暂缓的 ticket 时, 先重新评估 readiness 并更新 state role.

实现代码涉及 Module design 时, 调用 `codebase-design`, 应用 Deep Module design 和个人代码设计规范.

尽量调用 `tdd`, 在 pre-agreed Seams 上实现 behavior.

实现期间定期运行 typecheck 和 focused test files. 最后运行 full test suite.

完成后调用 `code-review` 审查本次工作. 根据审查结果完成本次范围内的必要修复, 重新验证并复查受影响的变更.

只将本次工作 commit 到当前 branch.

## Next Skills

结束时输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$implement`: 继续下一个 ready ticket, 或处理用户已接受的 review findings.
- `$to-tickets`: requirements coverage, ticket granularity 或 dependency graph 需要调整.
- `$grill-with-docs`: 实现暴露出新的 domain 或 architecture decision.
