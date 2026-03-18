# 贡献指南

感谢您对 HelpLook MCP Skill 项目的关注！

## 如何贡献

1. **Fork** 本仓库
2. **创建分支**：`git checkout -b feature/your-feature`
3. **提交更改**：`git commit -m "feat: 添加 xxx 功能"`
4. **推送分支**：`git push origin feature/your-feature`
5. **提交 Pull Request**

## 提交规范

- `feat`: 新功能
- `fix`: 修复问题
- `docs`: 文档更新
- `refactor`: 代码重构
- `test`: 测试相关

## 代码格式

- Python 代码遵循 PEP 8
- 使用 4 空格缩进

## 注意事项

- 请勿提交 `api-key.json` 或 `api-key-dev.json`，包含真实密钥的配置文件会被忽略
- 新增脚本时请同步更新 `references/tools.md` 和 `scripts/README.md`
