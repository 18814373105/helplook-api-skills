#!/usr/bin/env python3
"""GET /api/es - 全站关键字搜索"""
import sys
import json
from _common import get

if len(sys.argv) < 2:
    print("用法: es_search.py <keyword> [version_id] [page] [pagesize]", file=sys.stderr)
    print("  示例: es_search.py '用户登录' 0 1 10", file=sys.stderr)
    sys.exit(1)

keyword = sys.argv[1]
params = {"keyword": keyword}
if len(sys.argv) > 2:
    params["version_id"] = sys.argv[2]
if len(sys.argv) > 3:
    params["page"] = sys.argv[3]
if len(sys.argv) > 4:
    params["pagesize"] = sys.argv[4]

result = get("/api/es", params=params)
print(json.dumps(result, ensure_ascii=False, indent=2))
