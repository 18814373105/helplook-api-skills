---
name: helplook-content-api
description: >-
  调用 HelpLook Content API 进行文档管理。适用于集成 HelpLook 帮助中心、
  管理文章、目录、或用户提及 helplook API、content API、文档 API 时。
---

# HelpLook Content API Skill

HelpLook Content API 接口文档与 Python 调用脚本。

## 认证

除 `hot-list` 外，所有接口需认证：

- **Header**: `x-api-key: YOUR_API_KEY`
- **或 Query/Body**: `token=YOUR_API_KEY`

企业版 (PLAN_V2) 有效期内方可调用。

## 环境变量

| 变量 | 说明 | 默认 |
|------|------|------|
| `HELPLOOK_API_HOST` | API 根地址 | `https://api.helplook.net` |
| `HELPLOOK_API_KEY` | API Key（认证用） | 必填 |

## 接口列表

| 接口 | 方法 | 路径 | 脚本 |
|------|------|------|------|
| 文章列表 | GET | `/api/content` | `content_list.py` |
| 文章详情 | GET | `/api/content/:id` | `content_view.py` |
| 创建文档 | POST | `/api/content/create` | `content_create.py` |
| 更新文章 | PUT | `/api/content/:id` | `content_update.py` |
| 删除文章 | DELETE | `/api/content/:id` | `content_delete.py` |
| 上传文件 | POST | `/api/content/upload-file` | `content_upload_file.py` |
| 热门文章 | GET | `/api/content/hot-list` | `content_hot_list.py` |
| 获取文档列表 | GET | `/api/content/get-list` | `content_get_list.py` |
| 获取文档内容 | GET | `/api/content/get-content` | `content_get_content.py` |
| 更新文档内容 | POST | `/api/content/update-content` | `content_update_content.py` |
| 发布文章 | POST | `/api/content/publish-article` | `content_publish_article.py` |
| 导入文件 | POST | `/api/content/add-file` | `content_add_file.py` |
| 删除文章(批量) | POST | `/api/content/remove-article` | `content_remove_article.py` |
| 版本列表 | GET | `/api/content/get-version-list` | `content_get_version_list.py` |
| 全站搜索 | GET | `/api/es` | `es_search.py` |
| 全站搜索(token) | GET | `/api/es/search-tannant` | `es_search_tannant.py` |

## 使用脚本

```bash
# 设置环境变量
export HELPLOOK_API_KEY="your-api-key"
export HELPLOOK_API_HOST="https://api.helplook.net"  # 可选

# 示例：获取文章列表
python3 scripts/content_list.py

# 示例：获取文章详情（id 可为数字或 slug）
python3 scripts/content_view.py 123
python3 scripts/content_view.py my-article-slug

# 示例：热门文章（无需 API Key，需传 id 即 string_id）
python3 scripts/content_hot_list.py YOUR_STRING_ID
```

## 参数说明

### content_create / content_update

- `type`: 1=目录, 2=文章
- `name`: 名称，必填，≤200 字
- `status`: 1=草稿, 2=已发布, 3=仅更新用
- `parent_id`: 父级 ID，0 为根
- `editor_type`: 2=Markdown, 3=富文本
- `content`: 正文内容
- `metadata`: `{ slug, cover, seo_title, seo_keyword, seo_desc }`

### content_get_content / content_update_content

- `id` 或 `slug`: 二选一
- `version_slug`: 版本 slug（可选）
- `editor_type`: 2=Markdown, 3=富文本
- `is_write`: 1=同时发布, 2=仅保存草稿

## 详细参考

完整参数与错误码见 [references/content-api.md](references/content-api.md)。
