# HelpLook Content API 脚本

纯 Python 实现，无第三方依赖（仅使用标准库 `urllib`、`json`、`os`）。

## 环境变量

```bash
export HELPLOOK_API_KEY="your-api-key"
export HELPLOOK_API_HOST="https://api.helplook.net"  # 可选
```

## 运行方式

在 `helplook-api-skills` 根目录下：

```bash
python3 scripts/content_list.py
python3 scripts/content_view.py 123
python3 scripts/content_hot_list.py YOUR_STRING_ID  # 无需 API Key
```

或在 `scripts` 目录下：

```bash
cd scripts
python3 content_list.py
python3 content_view.py 123
```

## 脚本列表

| 脚本 | 说明 |
|------|------|
| content_list.py | 获取文章列表 |
| content_view.py | 获取文章详情 |
| content_create.py | 创建文档 |
| content_update.py | 更新文章 |
| content_delete.py | 删除文章 |
| content_upload_file.py | 上传文件 |
| content_hot_list.py | 热门文章（无需认证） |
| content_get_list.py | 获取文档列表 |
| content_get_content.py | 获取文档内容 |
| content_update_content.py | 更新文档内容 |
| content_publish_article.py | 发布文章 |
| content_add_file.py | 导入文件 |
| content_remove_article.py | 批量删除文章 |
| content_get_version_list.py | 获取版本列表 |
| es_search.py | 全站关键字搜索 |
| es_search_tannant.py | 全站搜索（需 token） |
