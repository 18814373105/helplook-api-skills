# HelpLook Content API 测试用例

基于重构后的 REST API 脚本整理。运行前请配置 `api-key.json` 或环境变量 `HELPLOOK_API_KEY`、`HELPLOOK_API_HOST`。

## 配置

```bash
# 复制并编辑
cp api-key.json.example api-key.json

# 或使用环境变量
export HELPLOOK_API_KEY="your-api-key"
export HELPLOOK_API_HOST="https://api.helplook.net"
```

---

## 1. content_list - 获取文章列表

**接口**：`GET /api/content`

**命令**：
```bash
cd scripts
python3 content_list.py
# 指定版本
python3 content_list.py 123
```

**预期**：返回 `{ data: { list: [...] } }`，树形结构含 id、name、slug、type、parent_id、child 等。

**测试结果**：✅ 通过

---

## 2. content_get_list - 获取文档列表

**接口**：`GET /api/content/get-list`

**命令**：
```bash
python3 content_get_list.py
python3 content_get_list.py 0   # version_id=0 为默认
```

**预期**：与 content_list 类似，返回树形文档列表。

**测试结果**：✅ 通过

---

## 3. content_view - 获取文章详情（按 ID 或 slug）

**接口**：`GET /api/content/:id`

**命令**：
```bash
python3 content_view.py 360
python3 content_view.py ljCSxI
```

**预期**：返回文章完整信息，含 content、draft_content。

**测试结果**：✅ 通过

---

## 4. content_get_content - 获取文档内容

**接口**：`GET /api/content/get-content`

**命令**：
```bash
python3 content_get_content.py 360
python3 content_get_content.py ljCSxI
# 指定版本
python3 content_get_content.py 360 v1.0
```

**参数**：`id` 或 `slug`，可选 `version_slug`。

**测试结果**：✅ 通过

---

## 5. content_get_version_list - 获取版本列表

**接口**：`GET /api/content/get-version-list`

**命令**：
```bash
python3 content_get_version_list.py
```

**预期**：返回 `{ data: [...] }`，多版本站点有数据。

**测试结果**：✅ 通过（当前站点无版本时返回空数组）

---

## 6. content_hot_list - 热门文章列表

**接口**：`GET /api/content/hot-list`（无需 API Key）

**命令**：
```bash
python3 content_hot_list.py gR2ILA
```

**参数**：`string_id` 为租户/站点标识。

**测试结果**：⚠️ 依赖站点配置，部分环境可能返回 505

---

## 7. content_create - 创建文档（目录或文章）

**接口**：`POST /api/content/create`

**命令**：
```bash
# 从 stdin 读取 JSON
echo '{"type":2,"name":"API测试","status":2,"parent_id":359,"editor_type":2,"content":"# 测试\n正文"}' | python3 content_create.py

# 从文件读取
python3 content_create.py examples/create_article.json
```

**参数**：
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | int | ✓ | 1=目录 2=文章 |
| name | string | ✓ | 标题 |
| status | int | | 1=发布 2=草稿，默认 2 |
| parent_id | int | | 父级 ID，0=根目录 |
| editor_type | int | | 2=Markdown 3=富文本 |
| content | string | | 正文，目录可空 |
| version_id | int | | 版本 ID |
| metadata | object | | slug、seo_title、seo_desc 等 |

**示例 JSON**：
```json
{
  "type": 2,
  "name": "示例文章",
  "status": 2,
  "parent_id": 0,
  "editor_type": 2,
  "content": "# 标题\n\n正文内容",
  "metadata": {
    "slug": "example-article",
    "seo_title": "示例 - SEO 标题"
  }
}
```

**测试结果**：✅ 通过

---

## 8. content_update - 更新文章

**接口**：`PUT /api/content/:id`

**命令**：
```bash
echo '{"name":"新标题","content":"# 新正文"}' | python3 content_update.py 360
python3 content_update.py 360 data.json
```

**参数**：`name`、`content` 等需符合后端校验（如 name 非空且 ≤200 字）。

**测试结果**：⚠️ 部分环境可能返回 402 校验错误，需确认后端要求

---

## 9. content_update_content - 仅更新正文

**接口**：`POST /api/content/update-content`

**命令**：
```bash
python3 content_update_content.py 360 2 "# 新正文" 2
```

**参数**：
- `id|slug`：文章 ID 或 slug
- `editor_type`：2=Markdown 3=富文本
- `content`：新正文
- `is_write`：1=发布 2=草稿（可选，默认 2）
- `version_id`：版本 ID（可选）

**测试结果**：✅ 通过

---

## 10. content_publish_article - 发布文章

**接口**：`POST /api/content/publish-article`

**命令**：
```bash
python3 content_publish_article.py 360
```

**预期**：返回 `{ data: { id, slug } }`。

**测试结果**：✅ 通过

---

## 11. content_delete - 删除文章

**接口**：`DELETE /api/content/:id`

**命令**：
```bash
python3 content_delete.py 360
```

**预期**：返回 `{ data: { ids } }`。

**测试结果**：✅ 通过

---

## 12. content_remove_article - 批量删除

**接口**：`POST /api/content/remove-article`

**命令**：
```bash
python3 content_remove_article.py 360 361 362
echo '[360,361,362]' | python3 content_remove_article.py
```

**参数**：`ids` 数组。

**测试结果**：✅ 通过

---

## 13. content_upload_file - 上传文件

**接口**：`POST /api/content/upload-file`（multipart）

**命令**：
```bash
python3 content_upload_file.py /path/to/file.pdf
python3 content_upload_file.py file.pdf 0 0   # parent_id version_id
```

**测试结果**：未测试（需本地文件）

---

## 14. content_add_file - 导入文件（CMS 模式）

**接口**：`POST /api/content/add-file`（multipart）

**命令**：
```bash
python3 content_add_file.py /path/to/file.pdf
python3 content_add_file.py file.pdf 0   # version_id
```

**测试结果**：未测试（需本地文件）

---

## 测试结果汇总

| 脚本 | 接口 | 状态 |
|------|------|------|
| content_list | GET /api/content | ✅ |
| content_get_list | GET /api/content/get-list | ✅ |
| content_view | GET /api/content/:id | ✅ |
| content_get_content | GET /api/content/get-content | ✅ |
| content_get_version_list | GET /api/content/get-version-list | ✅ |
| content_hot_list | GET /api/content/hot-list | ⚠️ |
| content_create | POST /api/content/create | ✅ |
| content_update | PUT /api/content/:id | ⚠️ |
| content_update_content | POST /api/content/update-content | ✅ |
| content_publish_article | POST /api/content/publish-article | ✅ |
| content_delete | DELETE /api/content/:id | ✅ |
| content_remove_article | POST /api/content/remove-article | ✅ |
| content_upload_file | POST /api/content/upload-file | 未测试 |
| content_add_file | POST /api/content/add-file | 未测试 |

---

## curl 示例

```bash
# 基础配置
API_HOST="https://api.helplook.net"
API_KEY="your-api-key"

# 获取列表
curl -s -H "x-api-key: $API_KEY" "$API_HOST/api/content"

# 获取详情
curl -s -H "x-api-key: $API_KEY" "$API_HOST/api/content/360"

# 创建文章
curl -s -X POST -H "x-api-key: $API_KEY" -H "Content-Type: application/json" \
  -d '{"type":2,"name":"测试","status":2,"parent_id":0,"editor_type":2,"content":"# 测试"}' \
  "$API_HOST/api/content/create"

# 更新正文
curl -s -X POST -H "x-api-key: $API_KEY" -H "Content-Type: application/json" \
  -d '{"id":"360","editor_type":2,"content":"# 新正文","is_write":2}' \
  "$API_HOST/api/content/update-content"

# 发布
curl -s -X POST -H "x-api-key: $API_KEY" -H "Content-Type: application/json" \
  -d '{"id":"360"}' \
  "$API_HOST/api/content/publish-article"

# 删除
curl -s -X DELETE -H "x-api-key: $API_KEY" "$API_HOST/api/content/360"
```

---

## 一键只读测试

```bash
#!/bin/bash
cd "$(dirname "$0")/.."
echo "=== content_list ==="
python3 scripts/content_list.py | head -80
echo "=== content_get_version_list ==="
python3 scripts/content_get_version_list.py
echo "=== content_view 360 ==="
python3 scripts/content_view.py 360 | head -40
```
