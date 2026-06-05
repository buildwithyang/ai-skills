#!/usr/bin/env python3
"""
Fetch news using NewsAPI.

Usage:
    python3 news_api.py --query "tech" --sources bbc-news --limit 5

Requires NEWS_API_KEY environment variable.
Get a free API key at: https://newsapi.org/
"""

import os
import sys
import argparse
import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import URLError


NEWS_API_BASE = "https://newsapi.org/v2"


def fetch_top_headlines(api_key, query=None, sources=None, category=None, country=None, limit=10):
    """Fetch top headlines from NewsAPI."""
    params = {"apiKey": api_key, "pageSize": limit}
    
    if query:
        params["q"] = query
    if sources:
        params["sources"] = sources
    if category:
        params["category"] = category
    if country:
        params["country"] = country

    url = f"{NEWS_API_BASE}/top-headlines?{urlencode(params)}"
    
    try:
        req = Request(url, headers={"User-Agent": "latest-news-skill/1.0"})
        with urlopen(req, timeout=30) as response:
            data = json.loads(response.read())
    except URLError as e:
        print(f"Error fetching news: {e}", file=sys.stderr)
        sys.exit(1)

    if data.get("status") != "ok":
        print(f"API Error: {data.get('message', 'Unknown error')}", file=sys.stderr)
        sys.exit(1)

    return data.get("articles", [])


def fetch_everything(api_key, query, sources=None, from_date=None, to_date=None, sort_by="publishedAt", limit=10):
    """Fetch all news articles from NewsAPI."""
    params = {
        "apiKey": api_key,
        "q": query,
        "pageSize": limit,
        "sortBy": sort_by,
    }
    
    if sources:
        params["sources"] = sources
    if from_date:
        params["from"] = from_date
    if to_date:
        params["to"] = to_date

    url = f"{NEWS_API_BASE}/everything?{urlencode(params)}"
    
    try:
        req = Request(url, headers={"User-Agent": "latest-news-skill/1.0"})
        with urlopen(req, timeout=30) as response:
            data = json.loads(response.read())
    except URLError as e:
        print(f"Error fetching news: {e}", file=sys.stderr)
        sys.exit(1)

    if data.get("status") != "ok":
        print(f"API Error: {data.get('message', 'Unknown error')}", file=sys.stderr)
        sys.exit(1)

    return data.get("articles", [])


def main():
    parser = argparse.ArgumentParser(description="Fetch news via NewsAPI")
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--sources", "-s", help="Comma-separated source IDs")
    parser.add_argument("--category", "-c", help="Category (business, entertainment, general, health, science, sports, technology)")
    parser.add_argument("--country", help="2-letter country code")
    parser.add_argument("--from-date", help="From date (YYYY-MM-DD)")
    parser.add_argument("--to-date", help="To date (YYYY-MM-DD)")
    parser.add_argument("--sort-by", default="publishedAt", help="Sort by: relevancy, popularity, publishedAt")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Number of articles")
    parser.add_argument("--headlines", action="store_true", help="Fetch top headlines instead of everything")
    args = parser.parse_args()

    api_key = os.environ.get("NEWS_API_KEY")
    if not api_key:
        print("Error: NEWS_API_KEY environment variable not set", file=sys.stderr)
        print("Get a free API key at: https://newsapi.org/", file=sys.stderr)
        sys.exit(1)

    if args.headlines:
        articles = fetch_top_headlines(
            api_key,
            query=args.query,
            sources=args.sources,
            category=args.category,
            country=args.country,
            limit=args.limit,
        )
    else:
        if not args.query:
            print("Error: --query is required for everything endpoint", file=sys.stderr)
            sys.exit(1)
        articles = fetch_everything(
            api_key,
            query=args.query,
            sources=args.sources,
            from_date=args.from_date,
            to_date=args.to_date,
            sort_by=args.sort_by,
            limit=args.limit,
        )

    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article.get('title', 'No title')}")
        if article.get("publishedAt"):
            print(f"   Published: {article['publishedAt']}")
        if article.get("source", {}).get("name"):
            print(f"   Source: {article['source']['name']}")
        if article.get("description"):
            desc = article["description"][:200] + "..." if len(article["description"]) > 200 else article["description"]
            print(f"   Summary: {desc}")
        if article.get("url"):
            print(f"   Link: {article['url']}")


if __name__ == "__main__":
    main()
