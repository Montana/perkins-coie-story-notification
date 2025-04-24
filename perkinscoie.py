#!/usr/bin/env python3

import time
import feedparser

SEARCH_TERM = "Perkins Coie site:bloomberg.com"
RSS_FEED_URL = f"https://www.google.com/alerts/feeds/12345678901234567890/{SEARCH_TERM.replace(' ', '+')}"

RSS_FEED_URL = "https://news.google.com/rss/search?q=Perkins+Coie+site:bloomberg.com"

CHECK_INTERVAL = 300 
seen_links = set()

def fetch_alerts():
    feed = feedparser.parse(RSS_FEED_URL)
    new_items = []
    for entry in feed.entries:
        if entry.link not in seen_links:
            seen_links.add(entry.link)
            new_items.append((entry.title, entry.link))
    return new_items

def main():
    print("🔔 Monitoring Bloomberg for 'Perkins Coie' stories...\n")
    while True:
        try:
            new_articles = fetch_alerts()
            if new_articles:
                print(f"\n📰 {len(new_articles)} new article(s) found:\n")
                for title, link in new_articles:
                    print(f"- {title}\n  {link}\n")
            else:
                print("⏳ No new articles.")
        except Exception as e:
            print(f" Error fetching feed: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
