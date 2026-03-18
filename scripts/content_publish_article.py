#!/usr/bin/env python3
"""POST /api/content/publish-article - 发布文章"""
import sys
from _common import post

if len(sys.argv) < 2:
    print("用法: content_publish_article.py <id>", file=sys.stderr)
    sys.exit(1)
cid = sys.argv[1]
result = post("/api/content/publish-article", data={"id": cid})
print(__import__("json").dumps(result, ensure_ascii=False, indent=2))
