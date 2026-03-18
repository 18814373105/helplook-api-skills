"""HelpLook API 公共模块 - 纯 Python 实现，无第三方依赖"""
import os
import json
import urllib.request
import urllib.error
import urllib.parse

_DEFAULT_HOST = "https://api.helplook.net"


def _load_api_key_json():
    """从 api-key.json 加载配置（项目根目录）"""
    for base in (os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.getcwd()):
        path = os.path.join(base, "api-key.json")
        if os.path.isfile(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
    return None


def get_base_url():
    env = os.environ.get("HELPLOOK_API_HOST")
    if env:
        return env.rstrip("/")
    cfg = _load_api_key_json()
    return (cfg and cfg.get("api_host") or _DEFAULT_HOST).rstrip("/")


def get_api_key():
    env = os.environ.get("HELPLOOK_API_KEY")
    if env:
        return env
    cfg = _load_api_key_json()
    return (cfg and cfg.get("api_key")) or ""


def build_headers(api_key=None, content_type="application/json"):
    api_key = api_key or get_api_key()
    headers = {"x-api-key": api_key}
    if content_type:
        headers["Content-Type"] = content_type
    return headers


def request(method, path, data=None, params=None, headers=None, use_auth=True):
    base = get_base_url()
    url = f"{base}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)

    req_headers = dict(headers or {})
    if use_auth:
        key = get_api_key()
        if not key:
            raise ValueError("HELPLOOK_API_KEY 未设置")
        req_headers.setdefault("x-api-key", key)

    body = None
    if data is not None:
        if isinstance(data, dict):
            body = json.dumps(data).encode("utf-8")
        elif isinstance(data, bytes):
            body = data
        else:
            body = str(data).encode("utf-8")

    req = urllib.request.Request(url, data=body, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                return raw
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8") if e.fp else ""
        try:
            err = json.loads(body)
        except json.JSONDecodeError:
            err = {"message": body or str(e)}
        raise SystemExit(f"HTTP {e.code}: {err}")


def get(path, params=None):
    return request("GET", path, params=params)


def post(path, data=None, params=None, content_type="application/json"):
    return request("POST", path, data=data, params=params, headers={"Content-Type": content_type})


def put(path, data=None):
    return request("PUT", path, data=data)


def delete(path):
    return request("DELETE", path)
