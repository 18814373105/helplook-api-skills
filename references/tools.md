# HelpLook 工具参考

## article_list

获取知识库中所有文章和目录的树形列表。

**参数**：无

**返回**：`{ list: [...] }`，list 为树形结构，含 id、name、slug、type、parent_id、child 等。

---

## article_search

按关键词全文搜索站点文章。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| keyword | string | ✓ | 搜索关键词 |
| page | integer | | 页码，默认 1 |
| pagesize | integer | | 每页条数，默认 10 |

**返回**：`{ list, total, page, pagesize }`

---

## article_get

根据 ID 或 slug 获取单篇文章详情。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | integer/string | | 文章 ID 或 slug |
| slug | string | | 文章 slug，与 id 二选一 |

---

## article_create

新建文章或目录。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | ✓ | 标题 |
| type | integer | | 1=目录 2=文章，默认 2 |
| parent_id | integer | | 父级 ID，默认 0 |
| editor_type | integer | | 2=Markdown 3=富文本，默认 2 |
| content | string | | 正文，目录可空 |
| status | integer | | 1=发布 2=草稿，默认 2 |
| slug | string | | 自定义 URL 路径 |
| cover | string | | 封面 base64 或 URL |

---

## article_update

修改已有文章或目录的标题、正文、状态、父级等。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | integer/string | | 文章 ID 或 slug |
| slug | string | | 与 id 二选一 |
| name | string | ✓ | 新标题 |
| content | string | ✓ | 新正文 |
| editor_type | integer | | 2=Markdown 3=富文本 |
| status | integer | | 1=发布 2=草稿 3=回收站 |
| parent_id | integer | | 新父级，用于移动 |

---

## article_update_content

仅更新文章正文，不改标题等。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | integer/string | | 文章 ID |
| slug | string | | 与 id 二选一 |
| content | string | ✓ | 新正文 |
| editor_type | integer | | 2=Markdown 3=富文本 |
| is_write | integer | | 1=保存并发布 2=仅保存草稿 |

---

## article_publish

将草稿发布为正式文章。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | integer | ✓ | 文章 ID |

---

## article_delete

删除文章，支持单个或批量。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | integer/string/array | | 文章 ID 或 ID 数组 |
| ids | array | | 与 id 二选一 |

---

## article_version_list

获取知识库版本列表（若站点支持多版本）。

**参数**：无

---

## article_hot_list

获取站点配置的推荐/热门文章列表。

**参数**：无
