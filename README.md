# OpenCode Skills Repository

本仓库包含用于OpenCode AI助手的技能(Skills)集合。这些技能可以扩展OpenCode的功能，帮助处理特定任务。

## 可用技能

### 1. **jiandaoyun-api** - 简道云API开发专家
- **功能**: 简道云Open API开发专家，提供完整的接口文档（表单、数据、通讯录等）、鉴权方式、错误码及多语言代码示例
- **用途**: 简道云接口调用、插件开发、数据对接、错误排查
- **核心功能**: API查询、代码生成（Python/Node.js/cURL）、错误排查、Schema校验
- **包含模块**: 身份认证、表单接口、数据管理、Webhook、前端组件
- **使用示例**: "如何调用新增数据接口？"、"错误码40010解决方案"、"Python批量更新数据示例"
- **目录**: `jiandaoyun-api/`

### 2. **lowes-to-shipstation** - Lowes订单转ShipStation导入工具  
- **功能**: 将简道云导出的Lowes订单数据转换为ShipStation系统导入模板，支持CSV和Excel格式，自动处理尺寸取整、重量转换和多数量订单拆分
- **用途**: 订单数据处理、格式转换、电商订单管理
- **核心功能**: 完整工作流集成、双文件输出、格式转换、尺寸优化、重量转换、数量处理、编码支持、格式支持
- **使用方法**: 命令行工具（集成工具 `process_lowes_orders.py` 和独立工具 `convert.py`、`split_orders.py`）、OpenCode调用
- **输出文件**: 拆分后的订单数据Excel文件（`*_split.xlsx`）和ShipStation导入CSV文件（`*_shipstation.csv`）
- **目录**: `lowes-to-shipstation/`

## 安装方法

### 方法一：使用安装脚本（推荐）

```bash
# 克隆仓库
git clone https://github.com/sakuree/skills.git
cd skills

# 运行安装脚本
chmod +x install.sh
./install.sh
```

### 方法二：手动安装

```bash
# 克隆仓库
git clone https://github.com/sakuree/skills.git

# 创建技能目录（如果不存在）
mkdir -p ~/.config/opencode/skills/

# 复制技能到OpenCode配置目录
cp -r skills/jiandaoyun-api ~/.config/opencode/skills/
cp -r skills/lowes-to-shipstation ~/.config/opencode/skills/
```

### 方法三：创建符号链接（便于更新）

```bash
# 克隆仓库到本地
git clone https://github.com/sakuree/skills.git ~/.opencode-skills

# 创建符号链接
ln -sf ~/.opencode-skills/jiandaoyun-api ~/.config/opencode/skills/
ln -sf ~/.opencode-skills/lowes-to-shipstation ~/.config/opencode/skills/
```

## 使用方法

安装后，在OpenCode中可以通过`skill`工具调用这些技能：

```
# 在OpenCode对话中
skill({ name: "jiandaoyun-api" })

# 或者直接询问
"如何使用简道云API新增数据？"
"帮我转换Lowes订单数据为ShipStation格式"
```

## 验证安装

```bash
# 检查技能是否已安装
ls -la ~/.config/opencode/skills/

# 应该看到：
# jiandaoyun-api/
# lowes-to-shipstation/
```

## 添加新技能

要添加新技能到本仓库：

1. 在仓库根目录创建新技能文件夹，如 `new-skill-name/`
2. 在文件夹中创建 `SKILL.md` 文件（必须包含YAML frontmatter）
3. 添加相关支持文件（Python脚本、配置文件等）
4. 提交并推送到GitHub

技能文件夹结构示例：
```
new-skill-name/
├── SKILL.md          # 技能定义文件（必须）
├── skill.json        # 技能元数据（可选）
├── manifest.json     # 清单文件（可选）
├── *.py              # Python脚本（可选）
└── docs/             # 文档目录（可选）
```

## 更新技能

```bash
# 拉取最新版本
cd skills
git pull

# 重新安装（如果使用复制方式）
./install.sh
```

## 卸载技能

```bash
# 使用卸载脚本
./uninstall.sh

# 或手动删除
rm -rf ~/.config/opencode/skills/jiandaoyun-api
rm -rf ~/.config/opencode/skills/lowes-to-shipstation
```

## 文件结构

```
skills/
├── README.md                    # 本文件
├── install.sh                   # 安装脚本
├── uninstall.sh                 # 卸载脚本
├── jiandaoyun-api/              # 技能1
│   ├── SKILL.md                 # 技能定义
│   ├── skill.json               # 技能元数据
│   ├── manifest.json            # 清单文件
│   ├── query.py                 # 查询脚本
│   └── docs/                    # 详细文档
│       ├── 01_Core_API/
│       ├── 02_Auth_Config/
│       ├── 03_Python_Implementation/
│       ├── 04_Webhooks/
│       └── 05_Advanced_Fields/
└── lowes-to-shipstation/        # 技能2
    ├── SKILL.md                 # 技能定义
    ├── skill.json               # 技能元数据
    ├── manifest.json            # 清单文件
    ├── convert.py               # 基础转换脚本
    ├── convert_modified.py      # 优化版本转换脚本
    ├── process_lowes_orders.py  # 集成工具（完整工作流）
    ├── split_orders.py          # 订单拆分工具
    └── query.py                 # 查询脚本
```

## 贡献指南

1. Fork本仓库
2. 创建新分支：`git checkout -b feature/new-skill`
3. 添加新技能或改进现有技能
4. 提交更改：`git commit -m "Add new skill: xxx"`
5. 推送到分支：`git push origin feature/new-skill`
6. 创建Pull Request

## 许可证

本仓库中的技能遵循各自的许可证，请查看各技能目录中的LICENSE文件（如果存在）。

## 支持

如有问题或建议，请：
1. 在GitHub Issues中提交问题
2. 或通过电子邮件联系

## 注意事项

- 确保OpenCode已正确安装和配置
- 某些技能可能需要额外的Python依赖包
- 定期更新以获取最新功能和修复