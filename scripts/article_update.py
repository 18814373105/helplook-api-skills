#!/usr/bin/env python3
"""修改文章或目录"""
import argparse
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="更新 HelpLook 文章/目录")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--id", help="文章 ID 或 slug")
    group.add_argument("-s", "--slug", help="文章 slug")
    parser.add_argument("name", help="新标题")
    parser.add_argument("content", help="新正文")
    parser.add_argument("--status", type=int, default=2, choices=[1, 2, 3],
                        help="1=发布 2=草稿 3=回收站")
    parser.add_argument("--editor-type", type=int, default=2, choices=[2, 3])
    parser.add_argument("--parent-id", type=int, help="新父级 ID")
    args = parser.parse_args()

    arguments = {
        "name": args.name,
        "content": args.content,
        "status": args.status,
        "editor_type": args.editor_type,
    }
    if args.id:
        arguments["id"] = args.id
    else:
        arguments["slug"] = args.slug
    if args.parent_id is not None:
        arguments["parent_id"] = args.parent_id

    url, api_key = get_config()
    result = call_tool(url, api_key, "article_update", arguments)
    print(json.dumps(result, ensure_ascii=False, indent=2))
