# PetGenie - 宠物生活指南网站

基于 Flask + Docker 的宠物服务网站，提供宠物知识库、表情识别和宠物地图等功能。

## 功能模块

1. 首页
   - 展示三个主要功能入口
   - 简洁的欢迎页面设计

2. 宠物知识库
   - 基于 Markdown 的内容管理
   - 支持文章分类和元数据
   - 响应式文章卡片布局

3. 宠物表情识别（开发中）
   - 实时表情分析
   - 情绪追踪报告
   - 行为建议指导

4. 宠物地图（开发中）
   - 宠物医院导航
   - 宠物友好场所
   - 紧急救助服务
   - 用户评价系统

## 内容管理

### 添加新文章

1. 在 `app/content/knowledge/` 目录下创建新的 .md 文件： 
```markdown
---
title: 文章标题
description: 文章描述
date: 2024-01-30
category: 分类名称
---
```


2. 文章会自动显示在知识库页面中

### 修改样式

1. 编辑 `app/static/css/main.css` 文件
2. 样式变更会自动应用到所有页面

## 备案说明

- 网站域名：petgenie.cn
- 备案号：沪ICP备2024105384号
- 所有页面都必须在底部显示备案信息
- 备案号需链接到：https://beian.miit.gov.cn/
