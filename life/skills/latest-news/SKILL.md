---
name: latest-news
description: Fetch and summarize latest news from multiple sources with cross-regional comparison, keyword filtering, consensus/divergence analysis, and daily summaries.
---

# Latest News

## Overview

Fetch news from **multiple independent sources** across different regions, then cross-compare to identify:
- **Consensus facts** — what all sources agree on
- **Divergence points** — where sources disagree or emphasize differently
- **Possible bias** — which source leans toward which side
- **Risk level** — based on escalation signals

**Focus on latest status only.** Skip historical context/event origins unless specifically requested.

## Quick Start

For general news, search broad keywords:
```python
results = web_search("latest tech news today", count=5)
```

For specific topics, include keywords:
```python
results = web_search("artificial intelligence news today", count=5)
```

## Workflow

### 1. Determine User Intent

- **General headlines** → Broad search, top stories
- **Specific topic** → Targeted search with keywords
- **Regional news** → Include location in query
- **Balanced view** → Use multi-source regional workflow (recommended)

### 2. Fetch News (Multi-Source)

**Mandatory for important topics:** Fetch from **at least 2-3 different source groups**.

| Method | Tool | Best For |
|--------|------|----------|
| **Web Search** | `web_search` | Breaking news, trending topics |
| **RSS Feeds** | `scripts/fetch_rss.py` | Specific sources, consistent formatting |
| **News APIs** | `scripts/news_api.py` | High-volume, filtered by category |
| **Direct Fetch** | `web_fetch` | Specific article URLs |

### 3. Cross-Compare & Summarize

For each source group, extract:
- Core events (what happened — latest status)
- Apparent stance / framing (how they present it)
- Key numbers/dates/facts

Then merge and produce:

```
## 共识事实 (Consensus)
- ...

## 分歧点 (Divergence)
- ...

## 可能偏差 (Possible Bias)
- ...

## 风险等级 (Risk Level)
🔴 High / 🟡 Medium / 🟢 Low
```

## Multi-Source Regional Workflow

### Source Groups

| Group | Sources | Characteristic |
|-------|---------|----------------|
| **west** | Reuters, BBC, AP | Western perspective |
| **middle_east** | Al Jazeera, The National, Gulf News | Regional/Gulf perspective |
| **china** | Xinhua, CGTN | Chinese perspective |
| **alternative** | TASS, RT, PressTV | Counter-narrative |

### Step 1: Fetch by Group

Use **identical keywords** across all groups for fair comparison:

```python
# Example: "US Iran tensions"
web_search("US Iran site:reuters.com OR site:bbc.com", count=5)
web_search("US Iran site:aljazeera.com OR site:thenationalnews.com", count=5)
web_search("US Iran site:xinhuanet.com OR site:cgtn.com", count=5)
```

### Step 2: Extract & Compare

For each article, note:
- **What facts are stated** (numbers, quotes, events)
- **What is omitted** (what other sources mention that this one doesn't)
- **Framing words** (loaded language, emotional tone)

### Step 3: Merge Output

**Format:**

```markdown
## 📰 最新状态 (Latest Status)
[Date] — [1-3 sentence overall summary capturing the essence]

### 🔴 关键动态 (Key Developments)
- [Event 1] — Source A, B
- [Event 2] — Source A only
- [Event 3] — Source B, C disagree on details

## 📊 交叉验证 (Cross-Verification)

### ✅ 共识事实 (Consensus)
- [Fact agreed by all sources]

### ⚠️ 分歧点 (Divergence)
| 方面 | Source A | Source B | Source C |
|------|----------|----------|----------|
| [Topic] | [View A] | [View B] | [View C] |

### 🎯 可能偏差 (Possible Bias)
- **Source A**: [leaning / framing]
- **Source B**: [leaning / framing]

### 📈 风险等级 (Risk Level)
🔴 High / 🟡 Medium / 🟢 Low
[Reasoning]

---
**Sources:** [links]
```

## Scripts

### scripts/fetch_rss.py

Fetch and parse RSS feeds from news sources.

Usage:
```bash
python3 scripts/fetch_rss.py <feed_url> [--limit N]
```

Example:
```bash
python3 scripts/fetch_rss.py https://feeds.bbci.co.uk/news/rss.xml --limit 5
```

### scripts/news_api.py

Fetch news using NewsAPI (requires API key).

Usage:
```bash
python3 scripts/news_api.py --query "tech" --sources bbc-news --limit 5
```

Requires `NEWS_API_KEY` environment variable.

## Scheduled Daily Summary (Cron)

To run automatically every day at 08:00:

```json
{
  "schedule": { "kind": "cron", "expr": "0 8 * * *", "tz": "Asia/Dubai" },
  "payload": {
    "kind": "agentTurn",
    "message": "latest-news 美伊局势"
  }
}
```

## Rules

1. **Always cross-compare** — Never rely on a single source for important topics
2. **Use identical keywords** across source groups for fair comparison
3. **Focus on latest status** — Skip historical context unless requested
4. **Highlight disagreements** — Divergence is often more informative than consensus
5. **Include source links** — Always cite sources for credibility
6. **Summarize in user's preferred language**
