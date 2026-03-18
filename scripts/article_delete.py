#!/usr/bin/env python3
"""删除文章"""
import argparse
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="删除 HelpLook 文章")
    parser.add_argument("ids", nargs="+", type=int, help="文章 ID 列表")
    args = parser.parse_args()

    arguments = {"id": args.ids} if len(args.ids) > 1 else {"id": args.ids[0]}
    url, api_key = get_config()
    result = call_tool(url, api_key, "article_delete", arguments)
    print(json.dumps(result, ensure_ascii=False, indent=2))
