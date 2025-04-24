#!/bin/bash

RSS_URL="https://news.google.com/rss/search?q=Perkins+Coie+site:bloomberg.com"
CHECK_INTERVAL=300
SEEN_FILE=".seen_perkins_coie"

touch "$SEEN_FILE"

while true; do
    curl -s "$RSS_URL" | grep -oP '(?<=<link>).*?(?=</link>)' | grep -v "^https://news.google.com" | while read -r link; do
        if ! grep -Fxq "$link" "$SEEN_FILE"; then
            echo "$link"
            echo "$link" >> "$SEEN_FILE"
            if command -v osascript > /dev/null; then
                osascript -e "display notification \"New Bloomberg article\" with title \"Perkins Coie Alert\" subtitle \"$link\""
            fi
        fi
    done
    sleep "$CHECK_INTERVAL"
done
