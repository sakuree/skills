#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lowes订单处理工具：自动拆分并转换为ShipStation格式

功能：
1. 读取Lowes订单Excel文件
2. 将Quantity > 1的订单拆分为多行（添加PO后缀）
3. 生成拆分后的Excel文件
4. 转换为ShipStation导入模板
5. 生成ShipStation CSV文件

用法:
    python process_lowes_orders.py input_file [options]

参数:
    input_file          输入的Lowes订单Excel文件 (.xlsx, .xls)
    
选项:
    --split-only        仅拆分订单，不转换为ShipStation格式
    --convert-only      仅转换为ShipStation格式，不进行拆分
    --no-split          转换时不进行数量拆分（直接使用原始数量）
    --output-dir DIR    输出目录（默认：当前目录）
    --prefix PREFIX     输出文件前缀（默认：使用输入文件名）
    --qty-col COL       数量列名（默认："Quantity"）
    --po-col COL        PO号列名（默认："PO Number"）
    --verbose, -v       显示详细输出
    --help, -h          显示帮助信息

示例:
    # 完整流程：拆分订单并转换为ShipStation格式（生成两个文件）
    python process_lowes_orders.py Lowes_Orders.xlsx
    
    # 仅拆分订单（生成拆分后的Excel文件）
    python process_lowes_orders.py Lowes_Orders.xlsx --split-only
    
    # 仅转换为ShipStation格式（假设订单已拆分）
    python process_lowes_orders.py Lowes_Orders.xlsx --convert-only
    
    # 指定输出目录和前缀
    python process_lowes_orders.py Lowes_Orders.xlsx --output-dir ./output --prefix processed

输出文件:
    1. [前缀]_split.xlsx - 拆分后的订单Excel文件
    2. [前缀]_shipstation.csv - ShipStation导入CSV文件

依赖:
    pandas, openpyxl (用于Excel文件)
    安装: pip install pandas openpyxl
"""

import sys
import os
import argparse
import traceback
from typing import List, Dict, Any, Tuple
import csv
import math
from datetime import datetime

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    print("错误: 未安装pandas，无法处理Excel文件。")
    print("请安装: pip install pandas openpyxl")
    sys.exit(1)

# --- ShipStation转换配置（从convert.py复制）---
SHIPSTATION_HEADERS = [
    "Order #", "Order Date", "Date Paid", "Order Total", "Amount Paid", "Tax", "Shipping Paid",
    "Shipping Service", "Height(in)", "Length(in)", "Width(in)", "Weight(oz)",
    "Custom Field 1", "Custom Field 2", "Custom Field 3", "Order Source",
    "Notes to the Buyer", "Notes from the Buyer", "Internal Notes", "Gift Message", "Gift Flag",
    "Buyer Full Name", "Buyer First Name", "Buyer Last Name", "Buyer Email", "Buyer Phone", "Buyer Username",
    "Recipient Full Name", "Recipient First Name", "Recipient Last Name", "Recipient Phone", "Recipient Company",
    "Address Line 1", "Address Line 2", "Address Line 3", "City", "State", "Postal Code", "Country Code",
    "Item SKU", "Item Name / Title", "Item Quantity", "Item Unit Price",
    "Item Weight (oz)", "Item Options", "Item Warehouse Location", "Item Marketplace ID"
]

# Lowes订单列名映射（与convert.py中的SOURCE_KEYS对应）
SOURCE_KEYS = {
    "PO": "PO Number",           # 订单号
    "SKU": "Item Number",        # 商品SKU
    "QTY": "Quantity",           # 数量
    "NAME": "Ship Name",         # 收货人姓名
    "ADDR1": "Ship Address_1",   # 地址行1
    "ADDR2": "Ship Address_2",   # 地址行2
    "CITY": "Ship City",         # 城市
    "STATE": "Ship State",       # 州
    "ZIP": "ZIP Code",           # 邮政编码
    "PHONE": "Ship Phone",       # 电话
    "LENGTH": "包裹长L (in)",    # 长度（英寸）
    "WIDTH": "包裹宽W (in)",     # 宽度（英寸）
    "HEIGHT": "包裹高H (in)",    # 高度（英寸）
    "WEIGHT_LB": "包裹重weight (lb)"  # 重量（磅）
}

def round_val(val: Any) -> int:
    """
    尺寸取整函数，与Web版本保持一致：
    1. 转换为浮点数
    2. 四舍五入
    3. 如果结果小于1，强制设为1
    """
    try:
        num = float(val)
    except (ValueError, TypeError):
        return ""
    
    # 四舍五入
    result = int(round(num))
    
    # 保底机制：如果是0（源数据比如0.4），强制改为1
    if result < 1:
        return 1
    return result

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="Lowes订单处理工具：自动拆分并转换为ShipStation格式",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""示例：
  完整流程（生成两个文件）：
    python process_lowes_orders.py Lowes_Orders.xlsx
  
  仅拆分订单：
    python process_lowes_orders.py Lowes_Orders.xlsx --split-only
  
  仅转换为ShipStation格式：
    python process_lowes_orders.py Lowes_Orders.xlsx --convert-only
  
  自定义输出：
    python process_lowes_orders.py Lowes_Orders.xlsx --output-dir ./output --prefix processed
"""
    )
    
    parser.add_argument("input_file", help="输入的Lowes订单Excel文件 (.xlsx, .xls)")
    
    # 处理模式选项（互斥）
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--split-only", action="store_true", help="仅拆分订单，不转换为ShipStation格式")
    mode_group.add_argument("--convert-only", action="store_true", help="仅转换为ShipStation格式，不进行拆分")
    mode_group.add_argument("--no-split", action="store_true", help="转换时不进行数量拆分（直接使用原始数量）")
    
    parser.add_argument("--output-dir", default=".", help="输出目录（默认：当前目录）")
    parser.add_argument("--prefix", help="输出文件前缀（默认：使用输入文件名）")
    parser.add_argument("--qty-col", default="Quantity", help="数量列名（默认：Quantity）")
    parser.add_argument("--po-col", default="PO Number", help="PO号列名（默认：PO Number）")
    parser.add_argument("--verbose", "-v", action="store_true", help="显示详细输出")
    
    return parser.parse_args()

def read_excel_file(file_path: str) -> pd.DataFrame:
    """读取Excel文件"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"输入文件不存在: {file_path}")
    
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ['.xlsx', '.xls']:
        raise ValueError(f"不支持的文件格式: {ext}，仅支持 .xlsx 和 .xls 格式")
    
    try:
        df = pd.read_excel(file_path, dtype=str)
        # 保留原始列名，但去除可能的空格
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        raise ValueError(f"读取Excel文件失败: {e}")

def validate_columns(df: pd.DataFrame, qty_col: str, po_col: str) -> None:
    """验证所需的列是否存在"""
    missing_cols = []
    if qty_col not in df.columns:
        missing_cols.append(qty_col)
    if po_col not in df.columns:
        missing_cols.append(po_col)
    
    if missing_cols:
        available_cols = list(df.columns)
        raise ValueError(
            f"找不到列名: {', '.join(missing_cols)}\n"
            f"可用的列名: {', '.join(available_cols)}\n"
            f"请使用 --qty-col 和 --po-col 参数指定正确的列名"
        )

def parse_quantity(value: Any) -> int:
    """解析数量值，处理各种格式"""
    if pd.isna(value):
        return 1
    
    # 尝试转换为字符串然后清理
    str_value = str(value).strip()
    if not str_value:
        return 1
    
    # 尝试提取数字（处理如 "2", "2.0", "2个" 等情况）
    try:
        # 移除非数字字符（保留小数点和负号）
        import re
        num_str = re.sub(r'[^\d.-]', '', str_value)
        if not num_str:
            return 1
        
        # 转换为浮点数然后取整
        num = float(num_str)
        # 四舍五入，但确保至少为1
        result = max(1, int(round(num)))
        return result
    except (ValueError, TypeError):
        return 1

def split_orders(df: pd.DataFrame, qty_col: str, po_col: str, verbose: bool = False) -> Tuple[pd.DataFrame, Dict]:
    """
    拆分订单数据
    返回新的DataFrame和统计信息
    """
    new_rows = []
    stats = {
        'original_rows': len(df),
        'total_split_rows': 0,
        'rows_split': 0,
        'rows_unchanged': 0
    }
    
    for idx, row in df.iterrows():
        try:
            qty = parse_quantity(row[qty_col])
            po_value = str(row[po_col]) if not pd.isna(row[po_col]) else ""
            
            if qty > 1:
                # 需要拆分
                for i in range(1, qty + 1):
                    new_row = row.copy()
                    new_row[qty_col] = 1
                    
                    # 添加PO后缀
                    if po_value:
                        new_row[po_col] = f"{po_value}-{i}"
                    else:
                        new_row[po_col] = f"ROW_{idx+1}-{i}"
                    
                    new_rows.append(new_row)
                
                stats['rows_split'] += 1
                stats['total_split_rows'] += qty
                
                if verbose:
                    print(f"行 {idx+1}: 数量 {qty} -> 拆分为 {qty} 行")
                
            else:
                # 数量为1或无效，保持原样
                new_rows.append(row)
                stats['rows_unchanged'] += 1
                stats['total_split_rows'] += 1
                
        except Exception as e:
            # 如果某行出错，至少保持原样
            print(f"警告: 处理第 {idx+1} 行时出错: {e}")
            new_rows.append(row)
            stats['rows_unchanged'] += 1
            stats['total_split_rows'] += 1
    
    # 创建新的DataFrame
    result_df = pd.DataFrame(new_rows)
    
    # 恢复原始列顺序
    result_df = result_df[df.columns]
    
    stats['processed_rows'] = len(result_df)
    return result_df, stats

def save_split_file(df: pd.DataFrame, output_path: str, verbose: bool = False) -> None:
    """保存拆分后的Excel文件"""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    try:
        df.to_excel(output_path, index=False)
        if verbose:
            print(f"拆分文件保存到: {output_path}")
            print(f"文件大小: {os.path.getsize(output_path)} 字节")
    except Exception as e:
        raise ValueError(f"保存拆分文件失败: {e}")

def convert_to_shipstation(df: pd.DataFrame, no_split: bool = False, verbose: bool = False) -> List[Dict[str, str]]:
    """
    将订单数据转换为ShipStation格式
    返回ShipStation格式的数据行列表
    """
    converted_rows = []
    stats = {
        'original_rows': len(df),
        'converted_rows': 0,
        'errors': 0
    }
    
    for idx, row in df.iterrows():
        try:
            # 获取PO号
            po = str(row.get(SOURCE_KEYS["PO"], "")).strip()
            if not po:
                stats['errors'] += 1
                continue
            
            # 处理数量（如果no_split为True，使用原始数量）
            qty_str = row.get(SOURCE_KEYS["QTY"], "1")
            try:
                qty_val = float(qty_str)
            except (ValueError, TypeError):
                qty_val = 1.0
            
            if no_split:
                # 不拆分，使用原始数量
                iterations = 1
                item_qty = max(1, round(qty_val))
            else:
                # 拆分（数量强制为1）
                iterations = max(1, round(qty_val))
                item_qty = 1
            
            # 处理重量（磅转盎司）
            weight_lb_str = row.get(SOURCE_KEYS["WEIGHT_LB"], "0")
            try:
                weight_lb = float(weight_lb_str)
            except (ValueError, TypeError):
                weight_lb = 0.0
            
            weight_oz = round(weight_lb * 16)
            
            # 处理尺寸
            length = round_val(row.get(SOURCE_KEYS["LENGTH"], ""))
            width = round_val(row.get(SOURCE_KEYS["WIDTH"], ""))
            height = round_val(row.get(SOURCE_KEYS["HEIGHT"], ""))
            
            # 其他字段
            today = datetime.now().strftime("%m/%d/%Y")
            
            # 基础字段
            name = str(row.get(SOURCE_KEYS["NAME"], "")).strip()
            phone = str(row.get(SOURCE_KEYS["PHONE"], "")).strip()
            addr1 = str(row.get(SOURCE_KEYS["ADDR1"], "")).strip()
            addr2 = str(row.get(SOURCE_KEYS["ADDR2"], "")).strip()
            city = str(row.get(SOURCE_KEYS["CITY"], "")).strip()
            state = str(row.get(SOURCE_KEYS["STATE"], "")).strip()
            zip_code = str(row.get(SOURCE_KEYS["ZIP"], "")).strip()
            sku = str(row.get(SOURCE_KEYS["SKU"], "")).strip()
            
            for i in range(1, iterations + 1):
                # 创建空行
                new_row = {header: "" for header in SHIPSTATION_HEADERS}
                
                # 填充数据
                if no_split:
                    # 不拆分，使用原始PO号
                    new_row["Order #"] = po
                    new_row["Item Quantity"] = str(item_qty)
                else:
                    # 拆分，添加后缀
                    new_row["Order #"] = f"{po}-{i}" if iterations > 1 else po
                    new_row["Item Quantity"] = "1"
                
                new_row["Order Date"] = today
                new_row["Date Paid"] = today
                new_row["Shipping Service"] = "Standard Shipping"
                new_row["Country Code"] = "US"
                new_row["Recipient Full Name"] = name
                new_row["Recipient Phone"] = phone
                new_row["Address Line 1"] = addr1
                new_row["Address Line 2"] = addr2
                new_row["City"] = city
                new_row["State"] = state
                new_row["Postal Code"] = zip_code
                new_row["Item SKU"] = sku
                new_row["Weight(oz)"] = str(weight_oz)
                new_row["Item Weight (oz)"] = ""
                new_row["Length(in)"] = str(length) if length != "" else ""
                new_row["Width(in)"] = str(width) if width != "" else ""
                new_row["Height(in)"] = str(height) if height != "" else ""
                
                converted_rows.append(new_row)
            
            stats['converted_rows'] += iterations
            
        except Exception as e:
            if verbose:
                print(f"警告: 第 {idx+1} 行转换失败: {e}")
            stats['errors'] += 1
            continue
    
    if verbose:
        print(f"ShipStation转换统计: 原始行 {stats['original_rows']}, 转换行 {stats['converted_rows']}, 错误 {stats['errors']}")
    
    return converted_rows

def save_shipstation_file(rows: List[Dict[str, str]], output_path: str, verbose: bool = False) -> None:
    """保存ShipStation CSV文件"""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=SHIPSTATION_HEADERS)
            writer.writeheader()
            writer.writerows(rows)
        
        if verbose:
            print(f"ShipStation文件保存到: {output_path}")
            print(f"文件大小: {os.path.getsize(output_path)} 字节")
            print(f"生成的列: {len(SHIPSTATION_HEADERS)} 列")
    except Exception as e:
        raise ValueError(f"保存ShipStation文件失败: {e}")

def main():
    """主函数"""
    args = parse_arguments()
    
    print("=" * 60)
    print("Lowes订单处理工具：自动拆分并转换为ShipStation格式")
    print("=" * 60)
    
    try:
        # 读取文件
        print(f"读取文件: {args.input_file}")
        df = read_excel_file(args.input_file)
        print(f"成功读取 {len(df)} 行数据")
        
        # 验证列名（如果不是仅转换模式）
        if not args.convert_only:
            print(f"使用配置 - 数量列: '{args.qty_col}', PO号列: '{args.po_col}'")
            validate_columns(df, args.qty_col, args.po_col)
        
        # 确定输出文件名前缀
        if args.prefix:
            prefix = args.prefix
        else:
            base_name = os.path.splitext(os.path.basename(args.input_file))[0]
            prefix = base_name
        
        # 确保输出目录存在
        os.makedirs(args.output_dir, exist_ok=True)
        
        # 处理模式
        if args.split_only:
            # 仅拆分模式
            print("\n" + "-" * 60)
            print("模式: 仅拆分订单")
            print("-" * 60)
            
            split_df, split_stats = split_orders(df, args.qty_col, args.po_col, args.verbose)
            
            # 保存拆分文件
            split_output = os.path.join(args.output_dir, f"{prefix}_split.xlsx")
            save_split_file(split_df, split_output, args.verbose)
            
            # 显示统计信息
            print("\n" + "=" * 60)
            print("拆分完成!")
            print(f"原始行数: {split_stats['original_rows']}")
            print(f"拆分行数: {split_stats['rows_split']}")
            print(f"未变行数: {split_stats['rows_unchanged']}")
            print(f"处理后总行数: {split_stats['processed_rows']}")
            
            if split_stats['rows_split'] > 0:
                avg_expansion = split_stats['processed_rows'] / split_stats['original_rows']
                print(f"平均扩展倍数: {avg_expansion:.2f}x")
            
            print(f"\n输出文件: {split_output}")
            
        elif args.convert_only:
            # 仅转换模式（不拆分）
            print("\n" + "-" * 60)
            print("模式: 仅转换为ShipStation格式（不拆分）")
            print("-" * 60)
            
            shipstation_rows = convert_to_shipstation(df, no_split=True, verbose=args.verbose)
            
            # 保存ShipStation文件
            ss_output = os.path.join(args.output_dir, f"{prefix}_shipstation.csv")
            save_shipstation_file(shipstation_rows, ss_output, args.verbose)
            
            print("\n" + "=" * 60)
            print("转换完成!")
            print(f"原始行数: {len(df)}")
            print(f"ShipStation行数: {len(shipstation_rows)}")
            print(f"\n输出文件: {ss_output}")
            
        else:
            # 完整流程：拆分 + 转换
            print("\n" + "-" * 60)
            print("模式: 完整流程（拆分订单并转换为ShipStation格式）")
            print("-" * 60)
            
            # 步骤1: 拆分订单
            print("\n步骤1: 拆分订单...")
            split_df, split_stats = split_orders(df, args.qty_col, args.po_col, args.verbose)
            
            # 保存拆分文件
            split_output = os.path.join(args.output_dir, f"{prefix}_split.xlsx")
            save_split_file(split_df, split_output, args.verbose)
            
            print(f"\n拆分完成!")
            print(f"原始行数: {split_stats['original_rows']}")
            print(f"拆分行数: {split_stats['rows_split']}")
            print(f"处理后总行数: {split_stats['processed_rows']}")
            
            # 步骤2: 转换为ShipStation格式
            print("\n步骤2: 转换为ShipStation格式...")
            shipstation_rows = convert_to_shipstation(split_df, no_split=False, verbose=args.verbose)
            
            # 保存ShipStation文件
            ss_output = os.path.join(args.output_dir, f"{prefix}_shipstation.csv")
            save_shipstation_file(shipstation_rows, ss_output, args.verbose)
            
            print("\n" + "=" * 60)
            print("处理完成!")
            print(f"原始行数: {split_stats['original_rows']}")
            print(f"拆分后行数: {split_stats['processed_rows']}")
            print(f"ShipStation行数: {len(shipstation_rows)}")
            
            if split_stats['rows_split'] > 0:
                avg_expansion = split_stats['processed_rows'] / split_stats['original_rows']
                print(f"平均扩展倍数: {avg_expansion:.2f}x")
            
            print(f"\n生成的文件:")
            print(f"1. 拆分后的Excel文件: {split_output}")
            print(f"2. ShipStation导入文件: {ss_output}")
        
        print("\n处理完成! 🎉")
        
    except Exception as e:
        print(f"\n错误: {e}")
        if args.verbose:
            traceback.print_exc()
        print("\n请检查:")
        print("1. 文件路径是否正确")
        print("2. Excel文件格式是否正确")
        print("3. 列名是否正确（区分大小写）")
        print("4. 使用正确的命令行参数")
        sys.exit(1)

if __name__ == "__main__":
    main()