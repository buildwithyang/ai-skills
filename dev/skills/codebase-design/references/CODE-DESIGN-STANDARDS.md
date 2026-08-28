# Code Design Standards

本文件是个人代码设计规范的唯一 source of truth.

这些规则用于 design, implementation 和 code review. 除非 repository 明确规定, 它们是需要结合 context 判断的 design rules, 不是机械 threshold.

## Rules

1. 优先处理 precondition, terminal, rejected, invalid 和 unsupported cases, 然后立即 return 或 raise.
2. `Long Function` 和 `Complicated Conditional` 触发 design review, 但不自动构成 violation.

## Review Test

Readable implementation 应满足:

- Reviewer 不打开下级 function, class, file 也能理解当前代码的主流程.
