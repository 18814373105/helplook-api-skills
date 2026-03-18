#!/usr/bin/env python3
"""POST /api/content/update-content - 更新文档内容"""
import sys
import json
from _common import post

if len(sys.argv) < 4:
    print("用法: content_update_content.py <id|slug> <editor_type> <content> [is_write] [version_id]", file=sys.stderr)
    print("  editor_type: 2=Markdown, 3=富文本; is_write: 1=发布, 2=草稿", file=sys.stderr)
    sys.exit(1)
arg = sys.argv[1]
data = {
    "id" if arg.isdigit() else "slug": arg,
    "editor_type": int(sys.argv[2]),
    "content": sys.argv[3],
    "is_write": int(sys.argv[4]) if len(sys.argv) > 4 else 2,
}
if len(sys.argv) > 5:
    data["version_id"] = sys.argv[5]
result = post("/api/content/update-content", data=data)
print(json.dumps(result, ensure_ascii=False, indent=2))
