# HelpLook Content API 参考

## 接口详情

### GET /api/content
获取文章列表（与 get-list 类似）

**Query**: `version_id` (可选)

### GET /api/content/:id
获取文章详情。`:id` 可为数字 ID 或 slug。

### POST /api/content/create
创建文档（目录或文章）

**Body (JSON)**:
- `type` (必填): 1=目录, 2=文章
- `name` (必填): 名称，≤200 字
- `status` (必填): 1=发布, 2=草稿
- `parent_id` (可选): 父级 ID，默认 0
- `version_id` (可选): 版本 ID
- `editor_type` (必填): 2=Markdown, 3=富文本
- `content` (必填): 正文
- `metadata` (可选): `{ slug, cover, seo_title, seo_keyword, seo_desc }`

### PUT /api/content/:id
更新文章/目录

**Body (JSON)**: 同 create，可部分更新

### DELETE /api/content/:id
删除文章

### POST /api/content/upload-file
上传文件

**Form**:
- `file`: 文件
- `parent_id` (可选)
- `version_id` (可选)

### GET /api/content/hot-list
热门文章列表，**无需认证**

**Query**: `id` (必填) - 租户 string_id

### GET /api/content/get-list
获取文档列表

**Query**: `version_id` (可选)

### GET /api/content/get-content
获取文档内容

**Query**:
- `id` 或 `slug`: 二选一
- `version_slug` (可选)

### POST /api/content/update-content
更新文档内容

**Body**:
- `id` 或 `slug`: 二选一
- `editor_type` (必填): 2 或 3
- `content` (必填)
- `is_write` (可选): 1=发布, 2=草稿，默认 2
- `version_id` (可选)

### POST /api/content/publish-article
发布文章

**Body**: `id` (必填)

### POST /api/content/add-file
导入文件（仅 CMS 模式）

**Form**: `file` (必填), `version_id` (可选)

### POST /api/content/remove-article
批量删除文章

**Body**: `ids` - 数组，文章 ID 列表

### GET /api/content/get-version-list
获取版本列表

### GET /api/es
全站关键字搜索

**Query**: `keyword` (必填), `version_id`, `page`, `pagesize`

### GET /api/es/search-tannant
全站关键字搜索（需 token 验证）

**Query**: 同 `/api/es`
