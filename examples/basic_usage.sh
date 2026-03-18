#!/bin/bash
# HelpLook Content API 基础使用示例

# 复制 api-key.json.example 为 api-key.json 并填入真实 API Key
# 或使用环境变量：
# export HELPLOOK_API_KEY="your-api-key"
# export HELPLOOK_API_HOST="https://api.helplook.net"

# 获取文章列表
python3 scripts/content_list.py

# 获取文章详情（数字 ID）
python3 scripts/content_view.py 123

# 获取文章详情（slug）
python3 scripts/content_view.py my-article-slug

# 热门文章（无需 API Key，需租户 string_id）
python3 scripts/content_hot_list.py YOUR_STRING_ID

# 获取版本列表
python3 scripts/content_get_version_list.py

# 完整测试用例见 examples/test_cases.md
