#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lowes订单转ShipStation导入模板
将简道云导出的Lowes订单数据转换为ShipStation系统可导入的CSV格式。

用法:
    python convert.py input_file output_file

支持格式:
    - CSV (UTF-8编码)
    - Excel (.xlsx, .xls)

依赖:
    pandas, openpyxl (用于Excel文件)
    安装: pip install pandas openpyxl
"""

import sys
import os
import csv
import math
from datetime import datetime
from typing import Dict, List, Any, Optional

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    print("警告: 未安装pandas，仅支持CSV文件处理。")
    print("建议安装: pip install pandas openpyxl")

# --- 配置 ---
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

def read_input_file(file_path: str) -> List[Dict[str, Any]]:
    """
    读取输入文件（CSV或Excel），返回字典列表
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"输入文件不存在: {file_path}")
    
    ext = os.path.splitext(file_path)[1].lower()
    
    if HAS_PANDAS:
        if ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path, dtype=str)
        elif ext == '.csv':
            # 尝试自动检测编码
            try:
                df = pd.read_csv(file_path, dtype=str, encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(file_path, dtype=str, encoding='gbk')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path, dtype=str, encoding='latin1')
        else:
            raise ValueError(f"不支持的文件格式: {ext}")
        
        # 替换NaN为空白字符串
        df = df.fillna('')
        # 转换为字典列表
        return df.to_dict('records')
    else:
        # 回退方案：仅处理CSV
        if ext != '.csv':
            raise ValueError("未安装pandas，仅支持CSV文件。请安装pandas以支持Excel文件。")
        
        data = []
        # 尝试多种编码
        encodings = ['utf-8', 'gbk', 'latin1']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # 确保所有键都是字符串
                        clean_row = {k.strip(): v.strip() if v is not None else '' for k, v in row.items()}
                        data.append(clean_row)
                break
            except UnicodeDecodeError:
                continue
        else:
            raise UnicodeDecodeError("无法解码CSV文件，请确保文件使用UTF-8、GBK或Latin1编码")
        
        return data

def convert_row(row: Dict[str, Any]) -> List[Dict[str, str]]:
    """
    转换单行数据，根据数量可能生成多行
    返回ShipStation格式的数据行列表
    """
    # 获取PO号，如果为空则跳过
    po = str(row.get(SOURCE_KEYS["PO"], "")).strip()
    if not po:
        return []
    
    # 处理数量
    qty_str = row.get(SOURCE_KEYS["QTY"], "1")
    try:
        qty_val = float(qty_str)
    except (ValueError, TypeError):
        qty_val = 1.0
    
    qty = max(1, round(qty_val))  # 数量取整，最小为1
    iterations = qty
    
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
    
    result_rows = []
    
    for i in range(1, iterations + 1):
        # 创建空行
        new_row = {header: "" for header in SHIPSTATION_HEADERS}
        
        # 填充数据
        new_row["Order #"] = f"{po}-{i}" if iterations > 1 else po
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
        new_row["Item Quantity"] = "1"
        new_row["Weight(oz)"] = str(weight_oz)
        new_row["Item Weight (oz)"] = ""
        new_row["Length(in)"] = str(length) if length != "" else ""
        new_row["Width(in)"] = str(width) if width != "" else ""
        new_row["Height(in)"] = str(height) if height != "" else ""
        
        result_rows.append(new_row)
    
    return result_rows

def convert_file(input_path: str, output_path: str) -> None:
    """
    主转换函数
    """
    print(f"读取文件: {input_path}")
    data = read_input_file(input_path)
    print(f"读取到 {len(data)} 行数据")
    
    converted_rows = []
    for idx, row in enumerate(data, 1):
        try:
            rows = convert_row(row)
            converted_rows.extend(rows)
        except Exception as e:
            print(f"警告: 第 {idx} 行转换失败: {e}")
            continue
    
    print(f"转换完成，生成 {len(converted_rows)} 行ShipStation数据")
    
    # 写入CSV文件
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=SHIPSTATION_HEADERS)
        writer.writeheader()
        writer.writerows(converted_rows)
    
    print(f"结果已保存: {output_path}")
    print(f"生成的列: {len(SHIPSTATION_HEADERS)} 列")

def main():
    """
    命令行入口点
    """
    if len(sys.argv) != 3:
        print(__doc__)
        print("\n参数错误!")
        print("用法: python convert.py <输入文件> <输出文件>")
        print("示例: python convert.py lowes_orders.csv shipstation_import.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        convert_file(input_file, output_file)
    except Exception as e:
        print(f"转换失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()