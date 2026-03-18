#!/usr/bin/env python3
"""
HelpLook MCP 客户端
通过 HTTP JSON-RPC 2.0 调用 MCP 工具
"""
import json
import os
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# 默认 MCP 接口地址（仅内部/本地测试可覆盖，不向用户暴露）
_DEFAULT_MCP_URL = "https://testing2-api.helplook.net/mcp/server"


def call_tool(
    url: str,
    api_key: str,
    tool_name: str,
    arguments: dict | None = None,
) -> dict:
    """调用 MCP 工具"""
    arguments = arguments or {}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments},
    }
    req = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except HTTPError as e:
        body = e.read().decode() if e.fp else ""
        raise SystemExit(f"HTTP {e.code}: {body}")
    except URLError as e:
        raise SystemExit(f"Request failed: {e.reason}")

    if "error" in data:
        raise SystemExit(f"MCP Error: {data['error']}")

    result = data.get("result", {})
    content = result.get("content", [])
    if result.get("isError"):
        text = content[0].get("text", "Unknown error") if content else "Unknown error"
        raise SystemExit(f"Tool error: {text}")

    if content and content[0].get("type") == "text":
        return json.loads(content[0]["text"])
    return result


def get_config() -> tuple[str, str]:
    """从环境变量或 api-key.json 获取 URL 和 API Key"""
    url = os.environ.get("HELPLOOK_MCP_URL", "").rstrip("/") or _DEFAULT_MCP_URL
    api_key = os.environ.get("HELPLOOK_API_KEY", "")

    if not api_key:
        # 尝试从 api-key.json 或 api-key-dev.json 加载
        script_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(script_dir)
        for name in ("api-key-dev.json", "api-key.json"):
            path = os.path.join(root_dir, name)
            if os.path.isfile(path):
                try:
                    with open(path, encoding="utf-8") as f:
                        cfg = json.load(f)
                    url = cfg.get("mcp_url") or url
                    api_key = cfg.get("api_key", api_key)
                    break
                except (json.JSONDecodeError, KeyError):
                    pass

    if not api_key:
        print("Usage: set HELPLOOK_API_KEY, or create api-key.json with api_key", file=sys.stderr)
        print("  export HELPLOOK_API_KEY=your-api-key", file=sys.stderr)
        print("  Or copy api-key.json.example to api-key.json and fill in api_key", file=sys.stderr)
        sys.exit(1)
    url = url.rstrip("/")
    if "/mcp/server" not in url:
        url = f"{url}/mcp/server"
    return url, api_key
