---
name: handoff
description: "将当前会话压缩为 handoff 文档, 供另一个 Agent 或新 session 接手."
argument-hint: "下一个 session 要做什么?"
disable-model-invocation: true
---

把当前会话整理成一份 handoff 文档, 让一个全新的 Agent 能继续这项工作. 接手方可以是新 session, 也可以是 Codex, Claude Code 等其他 Agent. 文档保存到操作系统的临时目录, 不放进当前 workspace.

文档中包含 "Suggested Skills" section, 列出下一个 Agent 应该调用的 skill.

已经记录在其他产物 (Spec, plan, ADR, issue, commit, diff) 中的内容, 用路径或 URL 引用, 不在文档中重复.

脱敏所有敏感信息, 例如 API key, 密码和个人身份信息.

如果用户传了参数, 把它视为下一个 session 的工作重点, 据此调整文档内容.

结束时输出文档的绝对路径, 以及一句可以直接粘贴给目标 Agent 的提示, 例如 `读取 <absolute-path> 并继续这项工作.`
