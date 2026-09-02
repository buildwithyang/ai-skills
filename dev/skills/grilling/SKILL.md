---
name: grilling
description: "通过严格追问检查方案的关键决策并形成 decision-complete plan. 仅在用户明确要求 grilling 或方案质询, 或另一个 Skill 明确调用时使用."
---

# Grilling

## Planning Preferences

- 每轮最多询问 3 个会明显改变方案的决策.
- 每个问题都给出推荐答案和最重要的取舍.
- 单文件或单命令即可确认的事实由当前 Agent 直接检查.
- 涉及多文件, 多模块或关系追踪的调查委派给 sub-agent. sub-agent 只返回结论, 证据位置和仍不确定的点.

## Completion

输出 decision-complete plan, 明确已定决策, 默认假设, 范围边界, 验证方式和显式延期项.

将规划结果返回调用方.
