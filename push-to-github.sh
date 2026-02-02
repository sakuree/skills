#!/bin/bash

# 推送技能到GitHub仓库的脚本

set -e

echo "=== 推送OpenCode技能到GitHub ==="
echo "仓库: https://github.com/sakuree/skills.git"
echo "当前目录: $(pwd)"
echo

# 检查是否在正确的目录
if [ ! -d ".git" ]; then
    echo "错误: 当前目录不是Git仓库"
    echo "请确保在 skills-repo 目录中运行此脚本"
    exit 1
fi

# 显示当前状态
echo "当前分支:"
git branch -v
echo
echo "远程仓库:"
git remote -v
echo
echo "未推送的提交:"
git log --oneline origin/main..main 2>/dev/null || echo "（无法获取远程信息）"
echo

# 选择推送方式
echo "请选择认证方式:"
echo "1) 使用SSH密钥 (已配置SSH密钥)"
echo "2) 使用HTTPS和个人访问令牌"
echo "3) 使用GitHub CLI (需要已安装gh)"
echo "4) 退出"
echo
read -p "请选择 [1-4]: " choice

case $choice in
    1)
        echo "使用SSH方式..."
        git remote set-url origin git@github.com:sakuree/skills.git
        ;;
    2)
        echo "使用HTTPS和个人访问令牌方式..."
        read -p "请输入GitHub用户名: " username
        read -sp "请输入个人访问令牌: " token
        echo
        git remote set-url origin "https://${username}:${token}@github.com/sakuree/skills.git"
        ;;
    3)
        echo "使用GitHub CLI..."
        if ! command -v gh &> /dev/null; then
            echo "错误: GitHub CLI (gh) 未安装"
            echo "请先安装: https://cli.github.com/"
            exit 1
        fi
        gh auth status || gh auth login
        ;;
    4)
        echo "退出"
        exit 0
        ;;
    *)
        echo "无效选择"
        exit 1
        ;;
esac

# 执行推送
echo
echo "正在推送到GitHub..."
if git push -u origin main; then
    echo
    echo "✅ 推送成功！"
    echo "仓库地址: https://github.com/sakuree/skills"
else
    echo
    echo "❌ 推送失败"
    echo "可能的原因:"
    echo "1. 认证失败 - 请检查SSH密钥或令牌"
    echo "2. 网络问题 - 请检查网络连接"
    echo "3. 权限不足 - 确保您有写入权限"
    exit 1
fi