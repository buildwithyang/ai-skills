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
