#!/usr/bin/env python3
"""仅更新文章正文"""
import argparse
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="更新 HelpLook 文章正文")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--id", help="文章 ID")
    group.add_argument("-s", "--slug", help="文章 slug")
    parser.add_argument("content", help="新正文内容")
    parser.add_argument("--is-write", type=int, default=2, choices=[1, 2],
                        help="1=保存并发布 2=仅保存草稿")
    parser.add_argument("--editor-type", type=int, default=2, choices=[2, 3])
    args = parser.parse_args()

    arguments = {
        "content": args.content,
        "is_write": args.is_write,
        "editor_type": args.editor_type,
    }
    if args.id:
        arguments["id"] = args.id
    else:
        arguments["slug"] = args.slug

    url, api_key = get_config()
    result = call_tool(url, api_key, "article_update_content", arguments)
    print(json.dumps(result, ensure_ascii=False, indent=2))
