#!/usr/bin/env python3
"""POST /api/content/create - 创建文档（目录或文章）"""
import sys
import json
from _common import post

# 从 stdin 读取 JSON，或使用示例
if sys.stdin.isatty():
    data = {
        "type": 2,
        "name": "示例文章",
        "status": 1,
        "parent_id": 0,
        "editor_type": 2,
        "content": "# 标题\n\n正文内容",
    }
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            data = json.load(f)
else:
    data = json.load(sys.stdin)

result = post("/api/content/create", data=data)
print(json.dumps(result, ensure_ascii=False, indent=2))
