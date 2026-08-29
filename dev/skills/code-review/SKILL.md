---
name: code-review
description: "Review working tree, branch, commit range 或 PR changes, 检查 requirements alignment 和 engineering risk. 当用户要求 code review, 或另一个 Skill 明确调用时使用."
---

# Code Review

以 read-only workflow 从两个独立 axis 审查同一个 change scope:

- **Requirements**: 是否正确且完整地实现 confirmed requirements.
- **Engineering**: 实现方式是否满足 correctness, architecture, contract, operational risk 和 verification 要求.

两个 axis 独立调查, 最后由主 Agent 验证 findings. 不用一个 axis 的 pass 掩盖另一个 axis 的 failure.

Review 本身不修改, stage, commit 或 push. 用户明确要求修复时再修改代码.

## Review Scope

1. 优先继承用户或 calling Skill 给出的 exact scope.
2. 用户要求 review current changes, 或 `implement` 调用时, 覆盖本次 task 的 staged, unstaged 和相关 untracked files. 排除已有 unrelated dirty changes. 无法可靠区分时, 只询问这一个 scope decision.
3. 用户指定 branch 或 PR 时, 先验证 ref, 再基于 merge-base review committed range. 用户指定 commit, range, files 或 diff 时, 严格使用该范围.
4. 记录 pinned `HEAD`, changed paths 和实际使用的 diff commands. Untracked files 需要单独枚举. Scope 为空时停止, 不生成虚假 review.
5. Review 期间 scope 发生变化时, 重新 pin scope 后再聚合结果.

## Evidence Sources

Requirements sources 按以下顺序查找:

1. Calling Skill 或用户提供的 ticket, formal Spec, confirmed plan 和 amendments.
2. 用户在当前 task 中明确说明的 behavior 和 constraints.
3. Branch, commits 或 repository 中明确关联的 issue 和 Spec.

没有可信 requirements source 时, 不阻塞 Engineering review. 将 Requirements 标记为 `Not assessed`, 不从 implementation 反推需求.

Engineering sources 包括:

- Applicable `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md` 和 documented repository standards.
- 相关 `CONTEXT.md`, ADR, public contracts 和 architecture constraints.
- [CODE-DESIGN-STANDARDS.md](../codebase-design/references/CODE-DESIGN-STANDARDS.md). Repository documented standards 优先于个人 defaults.

Existing patterns 只能作为 evidence, 不能自动视为 rule. Diff 涉及 Module design 时, 调用 `codebase-design` 应用 Deep Module discipline.

## Review Execution

- 多文件, 多模块或需要追踪 relationships 时, 并行委派 Requirements reviewer 和 Engineering reviewer. 单文件且局部的 change 由主 Agent 直接审查.
- 两个 reviewer 使用同一个 pinned scope, changed paths 和 evidence sources, 并检查受影响 callers, Interfaces, tests 和 surrounding code.
- Reviewer 不得再次调用 `code-review` 或继续 spawn sub-agents.
- Requirements reviewer 检查 missing 或 partial requirements, incorrect normal 和 failure behavior, scope creep, compatibility, migration, rollout 和 acceptance criteria coverage.
- Engineering reviewer 检查 correctness, architecture boundaries, Interface 和 API contracts, data model, compatibility, concurrency, security, operational risk, testability 和 verification gaps.
- 只报告具有 concrete impact 的问题. 不报告 style nit, generic improvement 或没有实际后果的 code smell.
- 对高价值 candidate finding 运行 proportional focused test 或 reproduction. 明确区分 static evidence, executed validation 和 unverified assumption.
- 主 Agent 复核每个 candidate finding, 删除 unsupported, duplicate, pre-existing 和 out-of-scope findings.

## Severity

- `P0`: Critical security, data loss 或 system-wide outage risk.
- `P1`: Merge blocker, 包括 expected path 上的 correctness, security 或 contract failure.
- `P2`: Concrete but bounded defect, compatibility risk 或 meaningful verification gap.

默认不报告 `P3` 和 nit.

## Output

Findings first, 分别放在 `## Requirements` 和 `## Engineering` 下, 各自按 severity 排序. 不合并两个 axis 的优先级.

每个 finding 包含:

- Severity, exact file 和 line.
- Trigger scenario 和 concrete impact.
- 对应 requirement, documented rule 或 violated invariant.
- Concise correction direction.

没有 finding 时写明 `No material findings`, 同时列出 residual risks 和未执行的 verification. 不声称绝对正确.

最后报告 reviewed scope, evidence sources 和 executed validation commands.
