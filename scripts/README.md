# HelpLook API Python 脚本

通过 HTTP 调用 HelpLook 接口的 Python 脚本，可用于自动化、测试或命令行操作。

## 配置

### 环境变量

```bash
export HELPLOOK_API_KEY=your-api-key
```

### 或使用 api-key.json

在项目根目录创建 `api-key.json`（可复制 `api-key.json.example`）：

```json
{
  "api_key": "your-api-key"
}
```

优先使用 `api-key-dev.json`（本地开发，已 gitignore）。

## 脚本列表

| 脚本 | 用途 | 示例 |
|------|------|------|
| article_list.py | 获取文章/目录列表 | `python article_list.py` |
| article_search.py | 关键词搜索 | `python article_search.py 用户指南 -p 1 -s 10` |
| article_get.py | 获取文章详情 | `python article_get.py -i 123` 或 `-s slug` |
| article_create.py | 新建文章/目录 | `python article_create.py "标题" -t 2 -c "# 内容"` |
| article_update.py | 修改文章 | `python article_update.py -i 123 "新标题" "新内容"` |
| article_update_content.py | 仅更新正文 | `python article_update_content.py -i 123 "新正文"` |
| article_publish.py | 发布草稿 | `python article_publish.py 123` |
| article_delete.py | 删除文章 | `python article_delete.py 123` 或 `123 456 789` |
| article_version_list.py | 版本列表 | `python article_version_list.py` |
| article_hot_list.py | 热门文章 | `python article_hot_list.py` |

## 运行方式

```bash
cd scripts
export HELPLOOK_API_KEY=xxx
python article_list.py
python article_search.py 测试
```

## 依赖

仅使用 Python 标准库，无需安装额外包。Python 3.7+ 即可。
