#!/usr/bin/env python3
"""DELETE /api/content/:id - 删除文章"""
import sys
from _common import delete

if len(sys.argv) < 2:
    print("用法: content_delete.py <id>", file=sys.stderr)
    sys.exit(1)
cid = sys.argv[1]
result = delete(f"/api/content/{cid}")
print(__import__("json").dumps(result, ensure_ascii=False, indent=2))
