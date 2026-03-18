#!/usr/bin/env python3
"""PUT /api/content/:id - 更新文章"""
import sys
import json
from _common import put

if len(sys.argv) < 2:
    print("用法: content_update.py <id> [data.json]", file=sys.stderr)
    sys.exit(1)
cid = sys.argv[1]
if len(sys.argv) > 2:
    with open(sys.argv[2], "r", encoding="utf-8") as f:
        data = json.load(f)
elif not sys.stdin.isatty():
    data = json.load(sys.stdin)
else:
    print("用法: content_update.py <id> [data.json] 或 echo '{}' | content_update.py <id>", file=sys.stderr)
    sys.exit(1)

result = put(f"/api/content/{cid}", data=data)
print(json.dumps(result, ensure_ascii=False, indent=2))
