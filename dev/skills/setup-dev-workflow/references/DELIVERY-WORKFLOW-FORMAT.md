# Delivery Workflow Format

写入 `docs/agents/delivery-workflow.md`. 使用 actual values 替换说明文本, 删除不适用字段和 placeholder.

```markdown
# Delivery Workflow

## Formal Spec

- Provider: GitHub | Markdown | GitLab | Jira
- Location: repository, project, issue key 或 path pattern
- Representation: issue type, label, document type 或 file convention
- Identifier: canonical reference format
- Access: CLI, MCP, API 或 filesystem
- Read: exact operation
- Publish: exact operation
- Amend: exact operation

## Issues

- Provider: GitHub | Markdown | GitLab | Jira
- Location: repository, project key 或 directory pattern
- Epic Representation: tracking issue, native Epic, issue type 或 file convention
- Ticket Representation: issue type 或 file convention
- Identifier: canonical reference format
- Access: CLI, MCP, API 或 filesystem
- Create: exact operation
- Read: exact operation
- Update: exact operation
- Close: exact operation

## Labels

| Role Group | Canonical Role | Tracker Label | Meaning |
| --- | --- | --- | --- |
| Artifact | `epic` | `type:epic` | Delivery scope and child ticket index |
| Category | `bug` | `bug` | Existing behavior is broken |
| Category | `enhancement` | `enhancement` | New behavior or improvement |
| State | `needs-triage` | `needs-triage` | Maintainer evaluation required |
| State | `needs-info` | `needs-info` | Waiting for reporter information |
| State | `ready-for-agent` | `ready-for-agent` | Fully specified and needs no further triage |
| State | `ready-for-human` | `ready-for-human` | Requires human implementation or judgment |
| State | `wontfix` | `wontfix` | Will not be actioned |

## Relationships And State

- Epic To Spec: Epic 到 Formal Spec 的 canonical link
- Ticket To Epic: native child relationship 或 explicit link fallback
- Ticket To Spec: ticket 到 Formal Spec 和 covered requirement IDs 的 canonical link
- Blocking: native relationship 或 explicit fallback field
- Open: provider-specific active state
- Closed: provider-specific completed state

## Constraints

- Formal Spec 只有一个 source of truth.
- Epic 只负责 delivery scope, progress 和 ticket hierarchy, 不复制 Formal Spec.
- Epic 使用 artifact role, 不使用 `ready-for-agent`.
- 每个 work ticket 最多一个 category role 和一个 state role. Skills 使用 canonical role, 再通过 mapping 查找 tracker label.
- `ready-for-agent` 表示不需要继续 triage, 不代表 blocker 已解除. Execution 仍需检查 blocking relationship.
- Issue 内容必须引用 covered requirement IDs.
- Provider 不支持 native blocking relationship 时, 使用 documented fallback, 不发明隐式 dependency.
```

## Provider Guidance

- 推荐组合: Formal Spec 使用 `docs/specs/<feature>.md`. Issues 使用 GitHub Issues. Epic 使用一个 GitHub tracking Issue 和 `type:epic`. Tickets 使用 canonical category 和 state roles, 优先使用 native sub-issues, 不可用时使用 checklist links.
- GitHub: 记录 `gh` operations, repository identity, Epic 和 ticket representation, 以及 native relationship availability.
- GitLab: 记录 `glab` operations, project identity, Issue representation 和 native relationship availability.
- Jira: 记录 site, project key, access mechanism, issue types, status semantics 和 link type. 不假设所有 Jira project 使用相同 workflow.
- Markdown: 使用 tracked repository files. Formal Spec 默认放在 `docs/specs/`, Issues 默认放在 `docs/issues/`. 一个 ticket 对应一个 file.

Setup 只记录 mapping 并验证 labels 是否存在, 不创建 remote labels. 缺失 labels 必须列入 external setup.
