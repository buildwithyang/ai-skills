---
name: to-tickets
description: "将已确认的 formal Spec 拆分为可独立验证的 tracer-bullet tickets, 并明确 requirements coverage 和 blocking dependencies."
disable-model-invocation: true
---

# To Tickets

将唯一 formal Spec 拆分为可执行的 ticket DAG. 每个 ticket 是可独立验证的 tracer bullet, 并声明真实的 blocking edges.

## Preconditions

- 必须提供已确认的 formal Spec location. 如果只有 conversation 或 plan, 停止并建议先使用 `to-spec`.
- 优先读取 `docs/agents/delivery-workflow.md` 中的 Issues, Labels 和 Relationships And State sections. 如果文件不存在, 再查找 repository 已有约定. 仍无法确认时, 只询问用户选择一个 destination, 并建议后续运行 `setup-dev-workflow` 持久化选择.
- 拆票阶段不新增 product requirement 或 architecture decision. 发现缺口时返回 `to-spec` 或 `grill-with-docs`.

## Process

1. 完整读取 formal Spec, 包括关联讨论和已确认 amendments. 同时检查相关 `CONTEXT.md`, ADR, project instructions 和当前 codebase.
2. 建立 requirement coverage map. 每个 In Scope requirement 必须由至少一个 ticket 覆盖, 每个 ticket 必须引用对应的 stable requirement ID.
3. 将工作拆成 tracer-bullet vertical slices. 每个 slice 应形成一个窄而完整的 behavior path, 能独立验证, 并适合在一个 fresh agent context 中完成.
4. 为每个 ticket 建立最小 blocking edges. 只记录真正阻止开始的 dependency, 保留能够并行推进的 frontier.
5. 向用户展示 draft DAG. 每个 ticket 给出 title, requirement IDs, outcome, verification 和 blocked by. 只询问会改变 granularity, dependency 或 delivery risk 的问题.
6. 用户确认后, 按配置创建或更新 Epic, 再按 dependency order 发布 tickets. 一个 ticket 对应一个 issue 或一个 local file.
7. 将所有 tickets 关联到 Epic 和 Formal Spec. 发布完成后返回 Epic location, ticket locations, initial frontier 和 requirements coverage summary. 不开始实现.

## Slicing Rules

- 优先按 end-to-end behavior 拆分, 不按 database, backend, frontend 或 tests 等 layer 水平拆分.
- Wide refactor 不强制拆成 vertical slices. 使用 expand-contract, 让新旧 form 暂时并存, 按 blast radius 分批迁移 callers, 最后删除旧 form.
- 每个 ticket 完成后必须保持 repository 可验证, 并产生可以观察的 incremental value 或 risk reduction.
- 必要的 prefactoring 可以成为前置 ticket, 但必须明确它解除的 blocker 和验证方式.
- ticket 大到无法在一个 fresh agent context 中完成时继续拆分. ticket 小到无法独立验证时合并到最近的 behavior slice.
- 避免把所有 tickets 串成线性 chain. 没有真实 blocking edge 的 tickets 应保持并行.

## Ticket Structure

### Title

用 behavior 或 outcome 命名, 不用 layer 或 activity 命名.

### Parent Spec

引用唯一 formal Spec 和本 ticket 覆盖的 requirement IDs.

### Outcome

描述完成后新增的 end-to-end behavior 或解除的 delivery risk.

### Acceptance Criteria

使用可观察且可验证的 criteria, 包括关键 failure behavior. 不重复 Spec 中与当前 slice 无关的内容.

### Verification

声明 testing seam, 必要的 regression coverage 和完成证据.

### Blocked By

列出真实阻塞本 ticket 开始的 ticket identifiers. 没有 blocker 时标记为 initial frontier.

### Architecture Constraints

只记录当前 slice 必须遵守的 module boundary, interface, API contract, data model 或 ADR. 不加入新的 architecture decision.

## Publishing Rules

- Epic 只汇总 delivery scope, progress 和 child tickets. 不复制 Formal Spec 内容.
- GitHub 默认使用一个 tracking Issue 表示 Epic, 并应用 configured `epic` artifact role. Epic 不应用 `ready-for-agent`.
- 每个 generated ticket 应用一个 configured category role 和 `ready-for-agent` state role. `ready-for-agent` 只表示无需继续 triage, blocking relationship 仍决定是否可以开始.
- 创建 Issue 前验证 configured labels 已存在. 缺失时在任何 remote write 前停止并报告 external setup.
- 优先使用 native sub-issues, 不可用时使用 checklist links.
- 真实 issue tracker 优先使用 native blocking relationship. 不支持时在 ticket body 中记录 `Blocked by`.
- Local destination 中一个 ticket 对应一个文件, 按 dependency order 编号.
- 保留 source Spec 或 parent issue 的状态和内容, 除非用户另有明确要求.
- 避免容易过期的 file paths 和完整 code snippets. Prototype 中表达 decision 所必需的最小 schema, state machine 或 type shape 可以保留并标记来源.

## Completion Gate

- 所有 In Scope requirement 都被覆盖, 且没有引入 Out of Scope work.
- Blocking graph 无环, dependency edge 最小, 并存在可立即开始的 initial frontier.
- Ticket 内容与 Spec, `CONTEXT.md`, ADR 和当前 codebase 一致.
- Epic 和 tickets 已按 configured relationship 关联, 且都能追溯到 Formal Spec.
- Epic 和 tickets 使用 configured canonical role mapping, 且没有 conflicting category 或 state labels.
- 用户已确认 draft DAG, 且所有 tickets 已发布.

## Next Skills

结束时从以下选项中输出当前适用的 1-3 个 next skills. 存在可用项时标记一个 Recommended, 没有时输出 `None`:

- `$implement`: 已有用户选定的 ready ticket.
- `$to-spec`: requirements coverage 或 Spec 需要修正.
- `$grill-with-docs`: 发现新的 domain 或 architecture decision.
- `$setup-dev-workflow`: Issue provider, relationship 或 label configuration 尚未持久化.
