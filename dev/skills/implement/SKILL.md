---
name: implement
description: "根据 Spec 或 tickets 实现工作."
disable-model-invocation: true
---

实现用户在 Spec 或 tickets 中描述的工作.

实现代码涉及 Module design 时, 调用 `codebase-design`, 应用 Deep Module design 和个人代码设计规范.

尽量调用 `tdd`, 在 pre-agreed Seams 上实现 behavior.

实现期间定期运行 typecheck 和 focused test files. 最后运行 full test suite.

完成后调用 `code-review` 审查本次工作.

只将本次工作 commit 到当前 branch.

## Next Skills

结束时输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$implement`: 继续下一个 ready ticket, 或处理用户已接受的 review findings.
- `$to-tickets`: requirements coverage, ticket granularity 或 dependency graph 需要调整.
- `$grill-with-docs`: 实现暴露出新的 domain 或 architecture decision.
