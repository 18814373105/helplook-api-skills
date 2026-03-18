#!/usr/bin/env python3
"""GET /api/content/:id - 获取文章详情，id 可为数字或 slug"""
import sys
from _common import get

if len(sys.argv) < 2:
    print("用法: content_view.py <id|slug>", file=sys.stderr)
    sys.exit(1)
cid = sys.argv[1]
result = get(f"/api/content/{cid}")
print(__import__("json").dumps(result, ensure_ascii=False, indent=2))
