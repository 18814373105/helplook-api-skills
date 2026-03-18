#!/usr/bin/env python3
"""按关键词搜索文章"""
import argparse
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="搜索 HelpLook 知识库文章")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("-p", "--page", type=int, default=1, help="页码")
    parser.add_argument("-s", "--pagesize", type=int, default=10, help="每页条数")
    args = parser.parse_args()

    url, api_key = get_config()
    result = call_tool(url, api_key, "article_search", {
        "keyword": args.keyword,
        "page": args.page,
        "pagesize": args.pagesize,
    })
    print(json.dumps(result, ensure_ascii=False, indent=2))
