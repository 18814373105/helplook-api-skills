#!/usr/bin/env python3
"""发布草稿文章"""
import argparse
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="发布 HelpLook 草稿文章")
    parser.add_argument("id", type=int, help="文章 ID")
    args = parser.parse_args()

    url, api_key = get_config()
    result = call_tool(url, api_key, "article_publish", {"id": args.id})
    print(json.dumps(result, ensure_ascii=False, indent=2))
