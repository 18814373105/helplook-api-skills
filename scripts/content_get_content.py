#!/usr/bin/env python3
"""GET /api/content/get-content - 获取文档内容"""
import sys
from _common import get

params = {}
if len(sys.argv) >= 2:
    arg = sys.argv[1]
    params["id" if arg.isdigit() else "slug"] = arg
if len(sys.argv) >= 3:
    params["version_slug"] = sys.argv[2]
if not params.get("id") and not params.get("slug"):
    print("用法: content_get_content.py <id|slug> [version_slug]", file=sys.stderr)
    sys.exit(1)
result = get("/api/content/get-content", params=params)
print(__import__("json").dumps(result, ensure_ascii=False, indent=2))
