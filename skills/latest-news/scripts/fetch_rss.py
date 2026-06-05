#!/usr/bin/env python3
"""
Fetch and parse RSS feeds from news sources.

Usage:
    python3 fetch_rss.py <feed_url> [--limit N]

Example:
    python3 fetch_rss.py https://feeds.bbci.co.uk/news/rss.xml --limit 5
"""

import sys
import argparse
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime


def fetch_rss(feed_url, limit=10):
    """Fetch and parse an RSS feed."""
    try:
        with urlopen(feed_url, timeout=30) as response:
            data = response.read()
    except URLError as e:
        print(f"Error fetching feed: {e}", file=sys.stderr)
        sys.exit(1)

    root = ET.fromstring(data)

    # Handle both RSS 2.0 and Atom formats
    if root.tag == "rss":
        channel = root.find("channel")
        items = channel.findall("item")[:limit]
    elif root.tag.endswith("feed"):
        items = root.findall(".//{http://www.w3.org/2005/Atom}entry")[:limit]
    else:
        print("Unsupported feed format", file=sys.stderr)
        sys.exit(1)

    news_items = []
    for item in items:
        if root.tag == "rss":
            title = item.find("title")
            link = item.find("link")
            pub_date = item.find("pubDate")
            description = item.find("description")

            news_items.append({
                "title": title.text if title is not None else "No title",
                "link": link.text if link is not None else "",
                "published": pub_date.text if pub_date is not None else "",
                "summary": description.text if description is not None else "",
            })
        else:  # Atom
            title = item.find("{http://www.w3.org/2005/Atom}title")
            link = item.find("{http://www.w3.org/2005/Atom}link")
            pub_date = item.find("{http://www.w3.org/2005/Atom}updated")
            summary = item.find("{http://www.w3.org/2005/Atom}summary")

            news_items.append({
                "title": title.text if title is not None else "No title",
                "link": link.get("href") if link is not None else "",
                "published": pub_date.text if pub_date is not None else "",
                "summary": summary.text if summary is not None else "",
            })

    return news_items


def main():
    parser = argparse.ArgumentParser(description="Fetch RSS news feeds")
    parser.add_argument("feed_url", help="URL of the RSS feed")
    parser.add_argument("--limit", type=int, default=10, help="Number of items to fetch (default: 10)")
    args = parser.parse_args()

    items = fetch_rss(args.feed_url, args.limit)

    for i, item in enumerate(items, 1):
        print(f"\n{i}. {item['title']}")
        if item["published"]:
            print(f"   Published: {item['published']}")
        if item["summary"]:
            # Truncate long summaries
            summary = item["summary"][:200] + "..." if len(item["summary"]) > 200 else item["summary"]
            print(f"   Summary: {summary}")
        if item["link"]:
            print(f"   Link: {item['link']}")


if __name__ == "__main__":
    main()
