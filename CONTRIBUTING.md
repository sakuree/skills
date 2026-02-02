# 贡献指南

感谢您对OpenCode Skills仓库的关注！我们欢迎任何形式的贡献，包括添加新技能、改进现有技能、修复错误或改进文档。

## 如何贡献

### 1. 报告问题
如果您发现任何问题或有改进建议，请通过GitHub Issues提交。

### 2. 添加新技能
要添加新技能，请遵循以下步骤：

#### 技能结构要求
每个技能必须包含以下结构：
```
skill-name/
├── SKILL.md          # 必须：技能定义文件（包含YAML frontmatter）
├── skill.json        # 可选：技能元数据
├── manifest.json     # 可选：清单文件
├── LICENSE           # 可选：许可证文件
├── *.py              # 可选：Python脚本
├── *.js              # 可选：JavaScript脚本
└── docs/             # 可选：文档目录
```

#### SKILL.md 文件规范
SKILL.md文件必须包含YAML frontmatter，格式如下：
```markdown
---
name: "skill-id"
description: "技能的详细描述，说明其功能和用途"
---

# 技能标题

## 功能概述
详细描述技能的功能...

## 使用方法
说明如何使用此技能...

## 示例
提供使用示例...
```

**注意**：
- `name`字段必须与目录名一致
- `description`字段应清晰描述技能的功能和用途
- 文件名必须为`SKILL.md`（全大写）

#### skill.json 文件规范（可选）
```json
{
  "id": "skill-id",
  "name": "技能显示名称",
  "description": "技能描述",
  "version": "1.0.0",
  "author": "作者名",
  "tags": ["标签1", "标签2"],
  "entry": "SKILL.md",
  "files": ["SKILL.md", "skill.json", "*.py"],
  "capabilities": {
    "feature1": true,
    "feature2": true
  },
  "requirements": ["package>=1.0.0"]
}
```

### 3. 改进现有技能
- 修复错误或问题
- 优化性能
- 改进文档
- 添加新功能

### 4. 改进文档
- 修复拼写或语法错误
- 改进说明的清晰度
- 添加更多示例
- 翻译为其他语言

## 开发流程

### 分支策略
1. Fork本仓库
2. 创建功能分支：`git checkout -b feature/your-feature-name`
3. 提交更改：`git commit -m "Add feature: description"`
4. 推送到分支：`git push origin feature/your-feature-name`
5. 创建Pull Request

### 提交消息规范
请使用清晰的提交消息：
- `feat:` 新功能
- `fix:` 修复错误
- `docs:` 文档更改
- `style:` 代码格式调整（不影响功能）
- `refactor:` 代码重构
- `test:` 添加或修改测试
- `chore:` 构建过程或辅助工具的变动

示例：
```
feat: add new skill for GitHub API integration
fix: correct error handling in convert.py
docs: update installation instructions
```

### 代码规范
- 保持代码简洁和可读
- 添加适当的注释
- 遵循现有的代码风格
- 确保技能在OpenCode中能正常工作

## 测试

在提交之前，请测试您的技能：

1. **本地测试**：使用安装脚本安装技能，然后在OpenCode中测试
2. **语法检查**：确保SKILL.md文件格式正确
3. **功能验证**：验证技能的所有功能都能正常工作

## 评审流程

1. 提交Pull Request后，维护者会进行代码审查
2. 可能需要根据反馈进行修改
3. 通过所有检查后，代码将被合并到主分支

## 许可证

通过向本仓库贡献代码，您同意您的贡献将遵循仓库的许可证（除非特别说明）。

## 需要帮助？

如果您有任何问题：
1. 查看现有文档和示例
2. 在GitHub Issues中提问
3. 查看已存在的技能作为参考

感谢您的贡献！🎉