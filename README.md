# HelpLook API Skills

OpenClaw Agent Skill for [HelpLook](https://www.helplook.net/) knowledge base article management.

## 简介

本 Skill 帮助 AI Agent 使用 HelpLook 接口管理知识库文章、目录、搜索等。

## 适用场景

- 已配置 HelpLook API Key
- 需要 AI 协助浏览、搜索、创建、编辑、发布或删除知识库文章
- 需要 AI 理解 HelpLook 文章结构（目录/文章、草稿/发布）

## 目录结构

```
helplook-api-skills/
├── SKILL.md           # 主技能文件（指令与快速参考）
├── README.md          # 本文件
├── CHANGELOG.md       # 变更日志
├── CONTRIBUTING.md    # 贡献指南
├── LICENSE            # MIT 许可证
├── api-key.json.example   # API 配置模板
├── api-key-dev.json   # 本地开发配置（gitignore）
├── pyproject.toml     # Python 项目配置
├── requirements.txt   # 依赖声明
├── references/        # 参考文档
│   └── tools.md      # 工具参数参考
├── examples/         # 示例
│   └── usage.md      # 调用示例
└── scripts/          # Python 可执行脚本
    ├── mcp_client.py  # API 客户端（内部实现）
    ├── article_list.py
    ├── article_search.py
    ├── article_get.py
    ├── article_create.py
    ├── article_update.py
    ├── article_update_content.py
    ├── article_publish.py
    ├── article_delete.py
    ├── article_version_list.py
    ├── article_hot_list.py
    └── README.md
```

## 安装

参考 OpenClaw 文档，将本仓库或 `SKILL.md` 配置到 Agent 技能目录。

## 配置

### 环境变量

```bash
export HELPLOOK_API_KEY=your-api-key
```

### 或使用配置文件

```bash
cp api-key.json.example api-key.json
# 编辑 api-key.json 填写 api_key
```

## 前置条件

1. **HelpLook 企业版**：需在 HelpLook 企业版中获取 API Key
2. **API Key**：在 HelpLook 后台生成并配置

## 工具列表

| 工具 | 用途 |
|------|------|
| article_list | 获取文章/目录树形列表 |
| article_search | 关键词全文搜索 |
| article_get | 获取单篇文章详情 |
| article_create | 新建文章或目录 |
| article_update | 修改文章/目录 |
| article_update_content | 仅更新正文 |
| article_publish | 发布草稿 |
| article_delete | 删除文章 |
| article_version_list | 版本列表 |
| article_hot_list | 推荐/热门文章 |

## 许可证

MIT

## 相关链接

- [HelpLook](https://www.helplook.net/)
