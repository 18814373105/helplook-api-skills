# HelpLook 工具调用示例

## 搜索并获取文章

```
1. article_search({"keyword": "用户指南", "page": 1, "pagesize": 5})
2. 从返回的 list 中取 id 或 slug
3. article_get({"id": 123}) 或 article_get({"slug": "user-guide"})
```

## 创建文章

```
article_create({
  "name": "快速入门",
  "type": 2,
  "parent_id": 0,
  "content": "# 快速入门\n\n欢迎使用...",
  "status": 2,
  "editor_type": 2
})
```

## 创建目录

```
article_create({
  "name": "产品文档",
  "type": 1,
  "parent_id": 0,
  "content": "",
  "status": 2
})
```

## 创建子文章

```
1. article_list() 获取目录结构
2. 找到目标目录的 id
3. article_create({
     "name": "安装说明",
     "type": 2,
     "parent_id": 8167749,
     "content": "# 安装\n\n...",
     "status": 2
   })
```

## 更新草稿并发布

```
1. article_update_content({
     "id": 123,
     "content": "# 更新后的内容\n\n...",
     "is_write": 2
   })
2. article_publish({"id": 123})
```

## 批量删除

```
article_delete({"ids": [123, 456, 789]})
```
