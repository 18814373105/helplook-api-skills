#!/usr/bin/env python3
"""获取单篇文章详情"""
import argparse
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="获取 HelpLook 文章详情")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--id", help="文章 ID 或 slug")
    group.add_argument("-s", "--slug", help="文章 slug")
    args = parser.parse_args()

    arguments = {"id": args.id} if args.id else {"slug": args.slug}
    url, api_key = get_config()
    result = call_tool(url, api_key, "article_get", arguments)
    print(json.dumps(result, ensure_ascii=False, indent=2))
