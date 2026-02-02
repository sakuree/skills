# OpenCode Skills 仓库

此仓库包含两个OpenCode技能：

1. **jiandaoyun-api** - 简道云API开发专家
2. **lowes-to-shipstation** - Lowes订单转ShipStation导入工具

## 如何推送到GitHub仓库

已准备好本地仓库，包含所有技能文件。您需要将其推送到远程仓库 `https://github.com/sakuree/skills.git`。

### 方法1：使用SSH密钥（推荐）

如果您已设置SSH密钥：

```bash
cd /home/sayjonny/skills-repo
git remote set-url origin git@github.com:sakuree/skills.git
git push -u origin main
```

### 方法2：使用个人访问令牌（PAT）

1. 在GitHub上生成个人访问令牌（需要`repo`权限）
2. 使用以下命令：

```bash
cd /home/sayjonny/skills-repo
git remote set-url origin https://你的用户名:你的令牌@github.com/sakuree/skills.git
git push -u origin main
```

### 方法3：使用GitHub CLI

如果已安装GitHub CLI：

```bash
cd /home/sayjonny/skills-repo
gh auth login
git push -u origin main
```

### 方法4：手动配置凭据

```bash
cd /home/sayjonny/skills-repo
git config credential.helper store
git push -u origin main
# 第一次会提示输入用户名和密码（使用令牌作为密码）
```

## 技能详情

### jiandaoyun-api
- 位置：`jiandaoyun-api/`
- 功能：简道云Open API开发专家，提供完整的接口文档、鉴权方式、错误码及多语言代码示例

### lowes-to-shipstation  
- 位置：`lowes-to-shipstation/`
- 功能：将简道云导出的Lowes订单数据转换为ShipStation系统导入模板，支持尺寸取整、重量转换、多数量订单拆分

## 文件结构

```
skills-repo/
├── .git/
├── jiandaoyun-api/
│   ├── SKILL.md
│   ├── query.py
│   ├── skill.json
│   ├── manifest.json
│   ├── convert.py (注：实际在lowes-to-shipstation中)
│   └── docs/ (完整文档)
└── lowes-to-shipstation/
    ├── SKILL.md
    ├── convert.py
    ├── query.py
    ├── skill.json
    └── manifest.json
```

## 注意事项

- 已提交初始提交：`Add initial skills: jiandaoyun-api and lowes-to-shipstation`
- 仓库已配置用户信息：`opencode-assistant <opencode@example.com>`
- 如需更改用户信息：`git config user.name "您的姓名" && git config user.email "您的邮箱"`

## 验证推送

推送成功后，访问：https://github.com/sakuree/skills 查看仓库内容。