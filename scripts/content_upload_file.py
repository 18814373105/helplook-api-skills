#!/usr/bin/env python3
"""POST /api/content/upload-file - 上传文件"""
import sys
import os
import mimetypes
import urllib.request
import urllib.error
import json

from _common import get_base_url, get_api_key, build_headers


def upload(file_path, parent_id=0, version_id=0):
    base = get_base_url()
    api_key = get_api_key()
    if not api_key:
        raise ValueError("HELPLOOK_API_KEY 未设置")
    url = f"{base}/api/content/upload-file"
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
        f'Content-Disposition: form-data; name="parent_id"\r\n\r\n{parent_id}\r\n'
        f"--{boundary}\r\n"
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
        with urllib.request.urlopen(req, timeout=60) as resp:
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
        print("用法: content_upload_file.py <file_path> [parent_id] [version_id]", file=sys.stderr)
        sys.exit(1)
    fp = sys.argv[1]
    pid = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    vid = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    result = upload(fp, pid, vid)
    print(json.dumps(result, ensure_ascii=False, indent=2))
