---
name: helplook-article-tools
description: >-
  Guides the agent to use HelpLook API for knowledge base article management.
  Use when the user needs to list, search, create, update, publish, or delete articles.
  Applies to HelpLook docs, knowledge base, or article management.
---

# HelpLook 知识库文章管理

使用以下工具管理 HelpLook 知识库文章、目录、搜索等。

## 前置条件

- 已配置 HelpLook API Key（api_key）
- 仅企业版 HelpLook 支持该接口

## 工具选择

| 用户意图 | 使用工具 |
|----------|----------|
| 浏览/列出文章结构 | `article_list` |
| 按关键词搜索 | `article_search` |
| 获取单篇详情 | `article_get` |
| 新建文章或目录 | `article_create` |
| 修改标题/正文/状态 | `article_update` |
| 仅改正文 | `article_update_content` |
| 草稿发布上线 | `article_publish` |
| 删除文章 | `article_delete` |

## 常用参数

| 参数 | 含义 |
|------|------|
| `type` | 1=目录 2=文章 |
| `parent_id` | 父级目录 ID，0=根目录 |
| `editor_type` | 2=Markdown 3=富文本 |
| `status` | 1=已发布 2=草稿 3=回收站 |
| `is_write` | 1=保存并发布 2=仅保存草稿 |

## 调用流程建议

1. **先搜索再详情**：用户想找某篇文章时，先用 `article_search` 按关键词搜索，再用 `article_get` 获取详情
2. **创建前选父级**：新建文章时，用 `article_list` 获取目录结构，确定 `parent_id`
3. **草稿先更新再发布**：新建默认草稿，可多次 `article_update_content` 修改，最后用 `article_publish` 发布

## 脚本工具

scripts/ 目录提供可执行的 Python 脚本，用于命令行调用：

```bash
cd scripts
export HELPLOOK_API_KEY=your-api-key

python article_list.py                    # 列表
python article_search.py "关键词"         # 搜索
python article_get.py -i 123              # 详情
python article_create.py "标题" -c "内容"  # 创建
python article_update.py -i 123 "标题" "内容"  # 更新
python article_update_content.py -i 123 "正文" # 仅更新正文
python article_publish.py 123             # 发布
python article_delete.py 123              # 删除
python article_version_list.py           # 版本列表
python article_hot_list.py                # 热门列表
```

配置：复制 `api-key.json.example` 为 `api-key.json` 并填写，或设置环境变量。详见 [scripts/README.md](scripts/README.md)

## 详细参考

- 完整参数说明见 [references/tools.md](references/tools.md)
- 调用示例见 [examples/usage.md](examples/usage.md)
