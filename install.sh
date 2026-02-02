#!/bin/bash

# OpenCode Skills 安装脚本
# 将本仓库中的技能安装到OpenCode配置目录

set -e

echo "=== OpenCode Skills 安装脚本 ==="
echo

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 函数：打印带颜色的消息
info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查是否在仓库根目录
if [ ! -f "README.md" ] || [ ! -d "jiandaoyun-api" ]; then
    error "请在仓库根目录运行此脚本"
    echo "当前目录: $(pwd)"
    exit 1
fi

# OpenCode配置目录
OPENDIR="$HOME/.config/opencode"
SKILLSDIR="$OPENDIR/skills"

# 创建目录
info "创建OpenCode技能目录..."
mkdir -p "$SKILLSDIR"

# 获取所有技能目录
skills=()
for dir in */; do
    if [ -f "${dir}SKILL.md" ]; then
        skills+=("${dir%/}")
    fi
done

if [ ${#skills[@]} -eq 0 ]; then
    error "未找到有效的技能目录（需要包含SKILL.md文件）"
    exit 1
fi

info "找到 ${#skills[@]} 个技能: ${skills[*]}"

# 安装选项
echo
echo "请选择安装方式:"
echo "1) 复制文件（推荐，独立副本）"
echo "2) 创建符号链接（便于更新，但需保持原目录）"
echo "3) 查看当前已安装的技能"
echo "4) 退出"
echo
read -p "请选择 [1-4]: " choice

case $choice in
    1)
        info "使用复制方式安装..."
        for skill in "${skills[@]}"; do
            if [ -d "$SKILLSDIR/$skill" ]; then
                warn "技能 '$skill' 已存在，将被覆盖"
                rm -rf "$SKILLSDIR/$skill"
            fi
            cp -r "$skill" "$SKILLSDIR/"
            info "已安装: $skill"
        done
        ;;
    2)
        info "使用符号链接方式安装..."
        # 获取仓库绝对路径
        REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
        
        for skill in "${skills[@]}"; do
            if [ -e "$SKILLSDIR/$skill" ]; then
                warn "移除已存在的 '$skill'"
                rm -rf "$SKILLSDIR/$skill"
            fi
            ln -sf "$REPO_DIR/$skill" "$SKILLSDIR/$skill"
            info "已创建符号链接: $skill"
        done
        ;;
    3)
        info "当前已安装的技能:"
        if [ -d "$SKILLSDIR" ]; then
            ls -la "$SKILLSDIR/"
        else
            echo "技能目录不存在: $SKILLSDIR"
        fi
        exit 0
        ;;
    4)
        info "退出安装"
        exit 0
        ;;
    *)
        error "无效选择"
        exit 1
        ;;
esac

# 验证安装
echo
info "验证安装..."
for skill in "${skills[@]}"; do
    if [ -f "$SKILLSDIR/$skill/SKILL.md" ]; then
        echo -e "${GREEN}✓${NC} $skill: 安装成功"
    else
        echo -e "${RED}✗${NC} $skill: 安装失败"
    fi
done

# 显示使用说明
echo
echo "======================"
info "安装完成！"
echo
echo "使用方法:"
echo "1. 启动OpenCode: opencode"
echo "2. 在对话中调用技能:"
for skill in "${skills[@]}"; do
    echo "   - skill({ name: \"$skill\" })"
done
echo
echo "或直接询问相关问题，如:"
echo '   "如何使用简道云API新增数据？"'
echo '   "帮我转换Lowes订单数据"'
echo
echo "技能目录: $SKILLSDIR"
echo "======================"