#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lowes订单转ShipStation技能查询助手
Usage: python query.py <关键词>
"""

import os
import sys
import json

def show_help():
    """显示帮助信息"""
    print("Lowes订单转ShipStation导入工具")
    print("=" * 60)
    print("\n主要功能:")
    print("  1. 将简道云导出的Lowes订单数据转换为ShipStation CSV模板")
    print("  2. 自动处理尺寸取整、重量转换、多数量订单拆分")
    print("  3. 支持CSV和Excel格式")
    
    print("\n使用方法:")
    print("  转换订单: python convert.py <输入文件> <输出文件>")
    print("  查看帮助: python query.py --help")
    print("  字段映射: python query.py --fields")
    print("  版本信息: python query.py --version")
    
    print("\n示例:")
    print('  python convert.py "lowes_orders.csv" "shipstation_import.csv"')
    print('  python query.py "尺寸"')

def show_fields():
    """显示字段映射"""
    print("字段映射表:")
    print("=" * 60)
    
    fields = [
        ("PO Number", "Order #", "订单号，多数量时会添加后缀"),
        ("Item Number", "Item SKU", "商品SKU"),
        ("Quantity", "Item Quantity", "数量，会拆分为多个订单"),
        ("Ship Name", "Recipient Full Name", "收货人姓名"),
        ("Ship Address_1", "Address Line 1", "地址行1"),
        ("Ship Address_2", "Address Line 2", "地址行2"),
        ("Ship City", "City", "城市"),
        ("Ship State", "State", "州"),
        ("ZIP Code", "Postal Code", "邮政编码"),
        ("Ship Phone", "Recipient Phone", "联系电话"),
        ("包裹长L (in)", "Length(in)", "长度（英寸），自动取整"),
        ("包裹宽W (in)", "Width(in)", "宽度（英寸），自动取整"),
        ("包裹高H (in)", "Height(in)", "高度（英寸），自动取整"),
        ("包裹重weight (lb)", "Weight(oz)", "重量（磅转盎司）"),
    ]
    
    for src, dst, desc in fields:
        print(f"源字段: {src}")
        print(f"目标字段: {dst}")
        print(f"说明: {desc}")
        print("-" * 40)

def show_version():
    """显示版本信息"""
    skill_file = os.path.join(os.path.dirname(__file__), "skill.json")
    if os.path.exists(skill_file):
        with open(skill_file, 'r', encoding='utf-8') as f:
            skill_info = json.load(f)
            print(f"技能名称: {skill_info.get('name', 'N/A')}")
            print(f"版本: {skill_info.get('version', 'N/A')}")
            print(f"描述: {skill_info.get('description', 'N/A')}")
    else:
        print("技能信息文件不存在")

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    if command in ['--help', '-h']:
        show_help()
    elif command in ['--fields', '-f']:
        show_fields()
    elif command in ['--version', '-v']:
        show_version()
    else:
        keyword = command
        print(f"搜索关键词: '{keyword}'")
        print("=" * 50)
        
        # 简单关键词匹配
        if keyword in ["尺寸", "长度", "宽度", "高度"]:
            print("\n尺寸处理规则:")
            print("  1. 四舍五入: 所有尺寸值先进行四舍五入取整")
            print("  2. 保底值: 如果取整后结果小于1，强制设置为1")
            print("  示例: 0.4 → 1, 1.6 → 2, 0 → 1")
        elif keyword in ["重量", "weight"]:
            print("\n重量转换规则:")
            print("  1. 源数据单位为磅(lb)")
            print("  2. 转换为盎司(oz): 磅 × 16")
            print("  3. 结果四舍五入取整")
        elif keyword in ["数量", "quantity", "拆分"]:
            print("\n数量处理规则:")
            print("  1. 如果Quantity字段为小数，先四舍五入取整")
            print("  2. 根据数量拆分为多个独立订单")
            print("  3. 订单号格式: PO-1, PO-2, ...")
        elif keyword in ["安装", "依赖", "requirements"]:
            print("\n依赖安装:")
            print("  pip install pandas openpyxl")
            print("\n如果没有安装pandas，脚本仅支持CSV文件格式")
        else:
            print(f"\n未找到与'{keyword}'相关的具体信息")
            print("\n可用关键词:")
            print("  --help, --fields, --version")
            print("  尺寸, 重量, 数量, 安装")

if __name__ == '__main__':
    main()