#!/usr/bin/env python3
"""新建文章或目录"""
import argparse
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="创建 HelpLook 文章或目录")
    parser.add_argument("name", help="标题")
    parser.add_argument("-t", "--type", type=int, default=2, choices=[1, 2],
                        help="1=目录 2=文章")
    parser.add_argument("-p", "--parent-id", type=int, default=0, help="父级 ID")
    parser.add_argument("-c", "--content", default="", help="正文内容")
    parser.add_argument("--status", type=int, default=2, choices=[1, 2],
                        help="1=发布 2=草稿")
    parser.add_argument("--editor-type", type=int, default=2, choices=[2, 3],
                        help="2=Markdown 3=富文本")
    parser.add_argument("--slug", help="自定义 URL 路径")
    args = parser.parse_args()

    arguments = {
        "name": args.name,
        "type": args.type,
        "parent_id": args.parent_id,
        "content": args.content,
        "status": args.status,
        "editor_type": args.editor_type,
    }
    if args.slug:
        arguments["slug"] = args.slug

    url, api_key = get_config()
    result = call_tool(url, api_key, "article_create", arguments)
    print(json.dumps(result, ensure_ascii=False, indent=2))
