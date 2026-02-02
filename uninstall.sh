#!/bin/bash

# OpenCode Skills 卸载脚本
# 从OpenCode配置目录中移除本仓库安装的技能

set -e

echo "=== OpenCode Skills 卸载脚本 ==="
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

# OpenCode配置目录
OPENDIR="$HOME/.config/opencode"
SKILLSDIR="$OPENDIR/skills"

# 检查技能目录是否存在
if [ ! -d "$SKILLSDIR" ]; then
    info "技能目录不存在: $SKILLSDIR"
    echo "可能已经卸载或从未安装过。"
    exit 0
fi

# 获取本仓库的技能列表
skills=()
if [ -f "README.md" ]; then
    for dir in */; do
        if [ -f "${dir}SKILL.md" ]; then
            skills+=("${dir%/}")
        fi
    done
fi

if [ ${#skills[@]} -eq 0 ]; then
    warn "无法确定本仓库的技能列表"
    echo "请手动选择要卸载的技能。"
    
    # 显示所有已安装的技能
    echo
    info "当前已安装的技能:"
    installed_skills=()
    for skill_dir in "$SKILLSDIR"/*/; do
        if [ -d "$skill_dir" ]; then
            skill_name="$(basename "$skill_dir")"
            installed_skills+=("$skill_name")
            echo "  - $skill_name"
        fi
    done
    
    if [ ${#installed_skills[@]} -eq 0 ]; then
        info "没有已安装的技能"
        exit 0
    fi
    
    echo
    read -p "请输入要卸载的技能名称（用空格分隔多个技能，或输入'all'卸载所有）: " input_skills
    
    if [ "$input_skills" = "all" ]; then
        skills=("${installed_skills[@]}")
    else
        # 将输入转换为数组
        IFS=' ' read -r -a skills <<< "$input_skills"
    fi
fi

if [ ${#skills[@]} -eq 0 ]; then
    info "没有选择要卸载的技能"
    exit 0
fi

info "准备卸载以下技能: ${skills[*]}"

# 确认卸载
echo
read -p "确定要卸载这些技能吗？(y/N): " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    info "取消卸载"
    exit 0
fi

# 执行卸载
echo
for skill in "${skills[@]}"; do
    skill_path="$SKILLSDIR/$skill"
    
    if [ -e "$skill_path" ]; then
        # 检查是否是符号链接
        if [ -L "$skill_path" ]; then
            info "移除符号链接: $skill"
            rm -f "$skill_path"
        elif [ -d "$skill_path" ]; then
            info "删除目录: $skill"
            rm -rf "$skill_path"
        else
            warn "未知的文件类型: $skill_path"
        fi
    else
        warn "技能 '$skill' 不存在，跳过"
    fi
done

# 清理空目录
info "清理空目录..."
if [ -d "$SKILLSDIR" ] && [ -z "$(ls -A "$SKILLSDIR")" ]; then
    rmdir "$SKILLSDIR"
    info "已删除空的技能目录"
fi

# 最终验证
echo
info "卸载完成！"
echo
echo "剩余技能:"
if [ -d "$SKILLSDIR" ]; then
    ls -la "$SKILLSDIR/" 2>/dev/null || echo "（空目录）"
else
    echo "技能目录已完全移除"
fi