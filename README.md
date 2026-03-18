# HelpLook Content API Skill

HelpLook 内容 API 接口封装，提供 Skill 与纯 Python 调用脚本。

## 目录结构

```
helplook-api-skills/
├── SKILL.md              # Skill 定义
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── api-key.json.example  # API 配置示例
├── pyproject.toml
├── requirements.txt
├── examples/             # 使用示例
├── references/           # 接口参考文档
└── scripts/              # Python 调用脚本
```

## 快速开始

### 1. 配置 API Key

```bash
cp api-key.json.example api-key.json
# 编辑 api-key.json 填入真实 api_key
```

或使用环境变量：

```bash
export HELPLOOK_API_KEY="your-api-key"
export HELPLOOK_API_HOST="https://api.helplook.net"  # 可选
```

### 2. 运行脚本

```bash
# 获取文章列表
python3 scripts/content_list.py

# 获取文章详情
python3 scripts/content_view.py 123

# 热门文章（无需 API Key）
python3 scripts/content_hot_list.py YOUR_STRING_ID
```

## 接口与脚本映射

| 接口 | 脚本 |
|------|------|
| GET /api/content | content_list.py |
| GET /api/content/:id | content_view.py |
| POST /api/content/create | content_create.py |
| PUT /api/content/:id | content_update.py |
| DELETE /api/content/:id | content_delete.py |
| POST /api/content/upload-file | content_upload_file.py |
| GET /api/content/hot-list | content_hot_list.py |
| GET /api/content/get-list | content_get_list.py |
| GET /api/content/get-content | content_get_content.py |
| POST /api/content/update-content | content_update_content.py |
| POST /api/content/publish-article | content_publish_article.py |
| POST /api/content/add-file | content_add_file.py |
| POST /api/content/remove-article | content_remove_article.py |
| GET /api/content/get-version-list | content_get_version_list.py |
| GET /api/es | es_search.py |
| GET /api/es/search-tannant | es_search_tannant.py |

## 依赖

纯 Python 实现，仅使用标准库（`urllib`、`json`、`os`），无第三方依赖。

## License

MIT
