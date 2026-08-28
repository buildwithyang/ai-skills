---
name: grilling
description: "Plan mode guard. 仅在用户明确要求 grilling 或方案质询, 或另一个 Skill 明确调用时使用."
---

# Grilling

## Plan Mode Guard

先判断当前宿主是否已经处于原生 Plan mode.

- 已经处于 Plan mode 时, 直接继续规划.
- 尚未处于 Plan mode 时, 停止当前流程并提示用户切换. Codex 使用 `/plan` 或 `Shift+Tab`. Claude Code 使用 `/plan` 或 `Shift+Tab`.
- 无法判断当前模式时, 请用户确认.

不要声称已经替用户切换模式. 等用户完成切换并回复后再继续.

## Planning Preferences

- 每轮最多询问 3 个会明显改变方案的决策.
- 每个问题都给出推荐答案和最重要的取舍.
- 单文件或单命令即可确认的事实由当前 Agent 直接检查.
- 涉及多文件, 多模块或关系追踪的调查委派给 sub-agent. sub-agent 只返回结论, 证据位置和仍不确定的点.

## Completion

输出 decision-complete plan, 明确已定决策, 默认假设, 范围边界, 验证方式和显式延期项. 等待用户确认后再进入有影响的执行.

这个 Skill 不整理项目文档. 需要同步术语, `CONTEXT.md` 或 ADR 时, 由调用方同时调用 `domain-modeling`.
