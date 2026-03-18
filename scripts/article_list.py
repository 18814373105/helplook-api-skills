#!/usr/bin/env python3
"""获取知识库文章/目录树形列表"""
import json
import sys
from mcp_client import get_config, call_tool

if __name__ == "__main__":
    url, api_key = get_config()
    print(url, api_key)
    result = call_tool(url, api_key, "article_list", {})
    print(json.dumps(result, ensure_ascii=False, indent=2))
