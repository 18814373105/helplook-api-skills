#!/usr/bin/env python3
"""GET /api/content/get-list - 获取文档列表"""
import sys
from _common import get

version_id = sys.argv[1] if len(sys.argv) > 1 else "0"
params = {"version_id": version_id} if version_id != "0" else None
result = get("/api/content/get-list", params=params)
print(__import__("json").dumps(result, ensure_ascii=False, indent=2))
