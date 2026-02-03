#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Excel订单自动拆分工具
将Quantity > 1的订单拆分为多行，并在PO Number后添加后缀。

用法:
    python split_orders.py input_file [output_file] [--qty-col COLUMN] [--po-col COLUMN]

参数:
    input_file     输入的Excel文件 (.xlsx, .xls)
    output_file    输出的Excel文件 (可选，默认：原文件名_processed.xlsx)
    --qty-col      数量列名 (默认: "Quantity")
    --po-col       PO号列名 (默认: "PO Number")

示例:
    python split_orders.py orders.xlsx
    python split_orders.py orders.xlsx output.xlsx --qty-col "数量" --po-col "订单号"

依赖:
    pandas, openpyxl (用于Excel文件)
    安装: pip install pandas openpyxl
"""

import sys
import os
import argparse
from typing import List, Dict, Any
import traceback

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    print("错误: 未安装pandas，无法处理Excel文件。")
    print("请安装: pip install pandas openpyxl")
    sys.exit(1)

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="Excel订单自动拆分工具 - 将Quantity > 1的订单拆分为多行",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""示例:
  python split_orders.py orders.xlsx
  python split_orders.py orders.xlsx output.xlsx --qty-col "数量" --po-col "订单号"
  python split_orders.py orders.xlsx --qty-col "QTY" --po-col "PO"
"""
    )
    
    parser.add_argument("input_file", help="输入的Excel文件 (.xlsx, .xls)")
    parser.add_argument("output_file", nargs="?", help="输出的Excel文件 (可选)")
    parser.add_argument("--qty-col", default="Quantity", help="数量列名 (默认: Quantity)")
    parser.add_argument("--po-col", default="PO Number", help="PO号列名 (默认: PO Number)")
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

def split_orders(df: pd.DataFrame, qty_col: str, po_col: str, verbose: bool = False) -> pd.DataFrame:
    """
    拆分订单数据
    返回新的DataFrame
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

def main():
    """主函数"""
    args = parse_arguments()
    
    print("=" * 60)
    print("Excel订单自动拆分工具")
    print("=" * 60)
    
    try:
        # 读取文件
        print(f"读取文件: {args.input_file}")
        df = read_excel_file(args.input_file)
        print(f"成功读取 {len(df)} 行数据")
        print(f"列名: {', '.join(df.columns.tolist())}")
        
        # 验证列名
        print(f"使用配置 - 数量列: '{args.qty_col}', PO号列: '{args.po_col}'")
        validate_columns(df, args.qty_col, args.po_col)
        
        # 拆分订单
        print("\n开始拆分订单...")
        result_df, stats = split_orders(df, args.qty_col, args.po_col, args.verbose)
        
        # 显示统计信息
        print("\n" + "=" * 60)
        print("处理完成!")
        print(f"原始行数: {stats['original_rows']}")
        print(f"拆分行数: {stats['rows_split']}")
        print(f"未变行数: {stats['rows_unchanged']}")
        print(f"处理后总行数: {stats['processed_rows']}")
        print(f"总计生成: {stats['total_split_rows']} 行")
        
        if stats['rows_split'] > 0:
            avg_expansion = stats['processed_rows'] / stats['original_rows']
            print(f"平均扩展倍数: {avg_expansion:.2f}x")
        
        # 确定输出文件名
        if args.output_file:
            output_path = args.output_file
        else:
            # 生成默认输出文件名
            base_name = os.path.splitext(args.input_file)[0]
            output_path = f"{base_name}_processed.xlsx"
        
        # 确保输出目录存在
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        
        # 保存文件
        print(f"\n保存结果到: {output_path}")
        result_df.to_excel(output_path, index=False)
        print("文件保存成功!")
        
        # 显示前几行预览
        print("\n预览前3行:")
        print("-" * 60)
        preview_df = result_df.head(3)
        for col in preview_df.columns:
            print(f"{col}: {preview_df[col].tolist()}")
        print("-" * 60)
        
        if len(result_df) > 3:
            print(f"... 还有 {len(result_df) - 3} 行未显示")
        
        print("\n处理完成! 🎉")
        
    except Exception as e:
        print(f"\n错误: {e}")
        if args.verbose:
            traceback.print_exc()
        print("\n请检查:")
        print("1. 文件路径是否正确")
        print("2. Excel文件格式是否正确")
        print("3. 列名是否正确（区分大小写）")
        print("4. 使用 --qty-col 和 --po-col 参数指定正确的列名")
        sys.exit(1)

if __name__ == "__main__":
    main()