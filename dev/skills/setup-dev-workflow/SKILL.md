---
name: setup-dev-workflow
description: "为 repository 配置 Formal Spec, Epic, Issues 和 workflow labels. 仅在用户明确要求初始化或切换 Dev workflow 时使用."
disable-model-invocation: true
---

# Setup Dev Workflow

为一个 repository 建立 run-once delivery workflow configuration, 让 `to-spec`, `to-tickets` 和 `code-review` 不再重复猜测 artifacts 存放位置, hierarchy, label semantics 和访问方式.

只支持 GitHub, Markdown, GitLab 和 Jira. Formal Spec 与 Issues 分别选择 provider, 可以相同, 也可以不同.

唯一输出是 project-local `docs/agents/delivery-workflow.md`. 不修改 `AGENTS.md` 或 `CLAUDE.md`, 不创建 remote Issue, label, project 或 workflow state.

## Recommended Default

首次设置时将以下方案作为推荐答案, 但必须询问用户确认:

- Formal Spec 使用 tracked Markdown, 放在 `docs/specs/<feature>.md`.
- Issues 使用当前 GitHub repository 的 GitHub Issues.
- 一个 delivery scope 使用一个 GitHub tracking Issue 表示 Epic. Implementation issues 通过 native sub-issues 关联, 不可用时使用 checklist links.
- Label vocabulary 使用 `type:epic`, `bug`, `enhancement`, `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human` 和 `wontfix`.
- ADR 保存在 repository, 继续由 `domain-modeling` 管理, 不复制到 Epic 或 Issues.

不得仅根据 repository host 或 existing convention 推断用户已经接受推荐方案. GitHub remote 或 access 无法确认时, 在询问中说明 blocker, 不静默切换 provider.

## Explore

先检查可确认事实:

- `git remote`, repository host 和 current branch conventions.
- Existing Spec, Issue, ticket, ADR 和 `docs/agents/` conventions.
- GitHub, GitLab 或 Jira 的 project identity, access mechanism 和 read-only connectivity.
- Existing Issue labels 和它们已经承担的 workflow roles.
- Markdown tracking directories and naming patterns.
- Existing `docs/agents/delivery-workflow.md` and any custom sections.

不询问能够从 repository 或 available tools 直接确认的事实.

## Decisions

只确认会改变 artifact ownership 或 operations 的决策:

1. Formal Spec provider 和 representation.
2. Issue provider, Epic representation 和 ticket representation.
3. Workflow label vocabulary.

首次创建 `docs/agents/delivery-workflow.md` 时必须询问以上 3 个决策, 每个问题明确标注推荐答案. Label vocabulary 默认保留 canonical role names, 只有 existing tracker 已有等价 labels 时才推荐 mapping. Existing configuration 只询问 requested change 或缺失项. 每轮最多询问 3 个决策.

Provider-specific missing information:

- GitHub: repository, Spec representation, Epic representation, Issue relationship, label availability 和 `gh` access.
- GitLab: project, Spec representation, Issue relationship 和 `glab` access.
- Jira: site, project key, access mechanism, Spec issue type, ticket issue type 和 blocking link type.
- Markdown: tracked paths. 默认使用 `docs/specs/<feature>.md` 和 `docs/issues/<feature>/<NN>-<slug>.md`, 除非 repository 已有约定.

如果 selected provider 无法通过 available tool 读取, 将 access 标记为 unverified 并报告 blocker. 不擅自登录, 安装 integration 或改用其他 provider.

## Write

1. 读取 [DELIVERY-WORKFLOW-FORMAT.md](references/DELIVERY-WORKFLOW-FORMAT.md).
2. 生成完整 draft, 填入实际 values 和可执行 operations, 不保留 placeholder.
3. 向用户展示 draft 或 existing file diff, 等待明确确认.
4. 写入或更新 `docs/agents/delivery-workflow.md`. Existing file 中不属于 canonical sections 的 custom content 必须保留.
5. 验证 Formal Spec, Issues 和 Labels sections 都能回答 location, identifier, operations, Epic hierarchy, relationship semantics 和 canonical role mapping.

## Completion

返回 configuration path, 两个 selected providers, Epic representation, label mapping, access verification status 和仍需人工完成的 external setup. 不开始 `to-spec` 或 `to-tickets`.
