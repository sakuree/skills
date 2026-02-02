#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简道云API技能查询助手
Usage: python query.py <关键词>
"""

import os
import sys
import json
import glob
import re

def load_manifest():
    """加载技能清单"""
    with open('manifest.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def search_docs(keyword):
    """搜索文档"""
    results = []
    docs_path = 'docs'
    
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if keyword.lower() in content.lower() or keyword.lower() in file.lower():
                        # 提取标题
                        title = content.split('\n')[0] if content.startswith('#') else file
                        results.append({
                            'file': file_path,
                            'title': title.replace('#', '').strip(),
                            'preview': content[:200] + '...' if len(content) > 200 else content
                        })
    
    return results

def list_categories():
    """列出所有分类"""
    categories = {
        '01_Core_API': '核心API接口',
        '02_Auth_Config': '鉴权与配置',
        '03_Python_Implementation': 'Python实现',
        '04_Webhooks': 'Webhook配置',
        '05_Advanced_Fields': '高级字段处理'
    }
    return categories

def main():
    if len(sys.argv) < 2:
        print("简道云API技能查询助手")
        print("=" * 50)
        print("\n使用方法:")
        print("  python query.py <关键词>     - 搜索相关文档")
        print("  python query.py --list       - 列出所有分类")
        print("  python query.py --manifest   - 显示技能清单")
        print("\n示例:")
        print('  python query.py "新增数据"')
        print('  python query.py 通讯录')
        print('  python query.py webhook')
        return
    
    command = sys.argv[1]
    
    if command == '--list':
        print("文档分类:")
        for key, value in list_categories().items():
            print(f"  {key}: {value}")
    
    elif command == '--manifest':
        manifest = load_manifest()
        print(f"技能名称: {manifest.get('name', 'N/A')}")
        print(f"版本: {manifest.get('version', 'N/A')}")
        print(f"描述: {manifest.get('description', 'N/A')}")
        print(f"\n索引数量: {len(manifest.get('index', []))}")
        print(f"主题数量: {len(manifest.get('themes', {}).keys())}")
    
    else:
        keyword = command
        print(f"搜索关键词: '{keyword}'")
        print("=" * 50)
        
        results = search_docs(keyword)
        
        if results:
            print(f"\n找到 {len(results)} 个相关文档:\n")
            for i, result in enumerate(results[:10], 1):
                print(f"{i}. {result['title']}")
                print(f"   文件: {result['file']}")
                print(f"   预览: {result['preview'][:100]}...")
                print()
            
            if len(results) > 10:
                print(f"... 还有 {len(results) - 10} 个结果")
        else:
            print("\n未找到相关文档")
            print("\n建议:")
            print("  - 尝试使用更通用的关键词")
            print("  - 使用 python query.py --list 查看所有分类")

if __name__ == '__main__':
    main()