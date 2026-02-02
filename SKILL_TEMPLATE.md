# 技能模板

此文件提供了创建新OpenCode技能的模板。复制此模板并根据需要修改。

## 快速开始

1. 在仓库根目录创建新文件夹：`your-skill-name/`
2. 在该文件夹中创建`SKILL.md`文件
3. 使用以下模板内容
4. 添加相关支持文件

## SKILL.md 模板

```markdown
---
name: "your-skill-id"
description: "在此处填写技能的详细描述，说明其功能和用途。描述应具体明确，帮助用户理解何时使用此技能。"
---

# 技能名称

在此处填写技能的标题和简要介绍。

## 功能概述

详细描述技能的功能、特性和优势。

## 核心能力

- 能力1：描述
- 能力2：描述  
- 能力3：描述

## 使用方法

### 在OpenCode中调用
```
skill({ name: "your-skill-id" })
```

### 直接询问示例
- "如何使用此技能完成X任务？"
- "帮我处理Y问题"
- "解释Z功能的工作原理"

## 配置要求

如果有任何配置要求或依赖项，请在此处说明。

### 依赖包
```bash
pip install package1 package2
```

### 环境变量
```
export API_KEY=your_key
```

## 示例

### 示例1：基本使用
```python
# 代码示例
def example_function():
    pass
```

### 示例2：常见场景
描述常见使用场景和解决方法。

## 故障排除

### 常见问题
1. **问题1**：解决方案
2. **问题2**：解决方案

### 错误代码
- 错误A：解释和解决方法
- 错误B：解释和解决方法

## 更新日志

- v1.0.0 (YYYY-MM-DD)：初始版本
- v1.0.1 (YYYY-MM-DD)：修复了X问题

## 相关资源

- [官方文档](链接)
- [示例项目](链接)
- [社区讨论](链接)
```

## skill.json 模板（可选）

```json
{
  "id": "your-skill-id",
  "name": "技能显示名称",
  "description": "技能描述，与SKILL.md中的描述一致",
  "version": "1.0.0",
  "author": "您的名字",
  "tags": ["标签1", "标签2", "标签3"],
  "entry": "SKILL.md",
  "files": [
    "SKILL.md",
    "skill.json",
    "*.py",
    "*.js"
  ],
  "capabilities": {
    "feature1": true,
    "feature2": true,
    "feature3": true
  },
  "usage": {
    "example1": "使用示例1的描述",
    "example2": "使用示例2的描述"
  },
  "requirements": [
    "package1>=1.0.0",
    "package2>=2.0.0"
  ]
}
```

## 清单文件模板（可选）

```json
{
  "name": "技能名称",
  "type": "opencode-skill",
  "version": "1.0.0",
  "description": "技能描述",
  "main": "SKILL.md",
  "author": "您的名字 <email@example.com>",
  "license": "MIT",
  "keywords": ["opencode", "skill", "标签1", "标签2"],
  "repository": {
    "type": "git",
    "url": "https://github.com/username/repo"
  }
}
```

## 最佳实践

1. **命名规范**：使用小写字母和连字符，如`my-skill-name`
2. **描述清晰**：提供具体、明确的描述，帮助用户理解技能用途
3. **示例丰富**：提供多种使用示例和场景
4. **文档完整**：包括安装、配置、使用和故障排除指南
5. **测试充分**：确保技能在实际使用中能正常工作
6. **保持更新**：定期维护和更新技能内容

## 验证技能

创建技能后，请验证：

1. SKILL.md文件格式正确（包含有效的YAML frontmatter）
2. 技能名称与目录名一致
3. 所有链接和示例代码正确
4. 技能在OpenCode中能正常调用

## 提交技能

完成技能开发后：
1. 将技能文件夹添加到仓库
2. 更新`skills-manifest.json`文件（可选）
3. 提交Pull Request
4. 等待代码审查和合并