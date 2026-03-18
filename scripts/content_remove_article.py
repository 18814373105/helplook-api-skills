#!/usr/bin/env python3
"""POST /api/content/remove-article - 批量删除文章"""
import sys
import json
from _common import post

ids = sys.argv[1:] if len(sys.argv) > 1 else []
if not ids and not sys.stdin.isatty():
    ids = json.load(sys.stdin)
if not ids:
    print("用法: content_remove_article.py <id1> [id2] ... 或 echo '[1,2,3]' | content_remove_article.py", file=sys.stderr)
    sys.exit(1)
ids = [int(x) if str(x).isdigit() else x for x in ids]
result = post("/api/content/remove-article", data={"ids": ids})
print(json.dumps(result, ensure_ascii=False, indent=2))
