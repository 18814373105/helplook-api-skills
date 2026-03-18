#!/usr/bin/env python3
"""POST /api/content/add-file - 导入文件（仅 CMS 模式，需上传 file）"""
import sys
import os
import mimetypes
import urllib.request
import urllib.error
import json
from _common import get_base_url, get_api_key

def add_file(file_path, version_id=0):
    base = get_base_url()
    api_key = get_api_key()
    if not api_key:
        raise ValueError("HELPLOOK_API_KEY 未设置")
    url = f"{base}/api/content/add-file"
    with open(file_path, "rb") as f:
        content = f.read()
    filename = os.path.basename(file_path)
    mime = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
    boundary = "----WebKitFormBoundary" + os.urandom(16).hex()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode("utf-8") + content + (
        f"\r\n--{boundary}\r\n"
        f'Content-Disposition: form-data; name="version_id"\r\n\r\n{version_id}\r\n'
        f"--{boundary}--\r\n"
    ).encode("utf-8")
    headers = {
        "x-api-key": api_key,
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Content-Length": str(len(body)),
    }
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8") if e.fp else ""
        try:
            err = json.loads(body_err)
        except json.JSONDecodeError:
            err = {"message": body_err or str(e)}
        raise SystemExit(f"HTTP {e.code}: {err}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: content_add_file.py <file_path> [version_id]", file=sys.stderr)
        sys.exit(1)
    fp = sys.argv[1]
    vid = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    result = add_file(fp, vid)
    print(json.dumps(result, ensure_ascii=False, indent=2))
