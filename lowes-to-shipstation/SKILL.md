---
name: "lowes-to-shipstation"
description: "将简道云导出的Lowes订单数据转换为ShipStation系统导入模板。支持CSV和Excel格式，自动处理尺寸取整、重量转换和多数量订单拆分。"
---

# Lowes订单转ShipStation导入工具

本技能用于将从简道云导出的Lowes订单数据转换为ShipStation系统可识别的CSV导入模板。

## 功能特点

- **格式转换**: 将Lowes订单数据映射到ShipStation所需的52个字段
- **尺寸优化**: 自动对长宽高进行四舍五入，小于1的尺寸强制设为1（V7版本优化）
- **重量转换**: 自动将磅(lb)转换为盎司(oz)
- **数量处理**: 支持多数量订单拆分（如数量为3的订单会拆分为3个独立订单）
- **编码支持**: 自动检测CSV文件编码（UTF-8、GBK、Latin1）
- **格式支持**: 支持CSV和Excel（.xlsx, .xls）格式

## 使用方法

### 命令行使用

```bash
# 基本用法
python convert.py 输入文件 输出文件

# 示例
python convert.py lowes_orders.csv shipstation_import.csv
python convert.py lowes_orders.xlsx shipstation_output.csv
```

### 在OpenCode中调用

当用户需要转换Lowes订单数据时，可以直接调用此技能：

1. 确保已安装依赖：`pip install pandas openpyxl`
2. 使用技能提供的转换脚本
3. 或者直接询问技能如何使用

## 字段映射

源数据字段（简道云导出）与ShipStation字段的对应关系：

| 源字段 (Lowes) | ShipStation字段 | 说明 |
|----------------|-----------------|------|
| PO Number | Order # | 订单号，多数量时会添加后缀 |
| Item Number | Item SKU | 商品SKU |
| Quantity | Item Quantity | 数量，会拆分为多个订单 |
| Ship Name | Recipient Full Name | 收货人姓名 |
| Ship Address_1 | Address Line 1 | 地址行1 |
| Ship Address_2 | Address Line 2 | 地址行2 |
| Ship City | City | 城市 |
| Ship State | State | 州 |
| ZIP Code | Postal Code | 邮政编码 |
| Ship Phone | Recipient Phone | 联系电话 |
| 包裹长L (in) | Length(in) | 长度（英寸），自动取整 |
| 包裹宽W (in) | Width(in) | 宽度（英寸），自动取整 |
| 包裹高H (in) | Height(in) | 高度（英寸），自动取整 |
| 包裹重weight (lb) | Weight(oz) | 重量（磅转盎司） |

## 尺寸处理规则

与Web版本V7保持一致：

1. **四舍五入**: 所有尺寸值先进行四舍五入取整
2. **保底值**: 如果取整后结果小于1，强制设置为1
3. **示例**:
   - 0.4 → 1
   - 1.6 → 2
   - 0 → 1

## 依赖安装

```bash
pip install pandas openpyxl
```

如果没有安装pandas，脚本仅支持CSV文件格式。

## 常见问题

### 1. 文件编码问题
如果CSV文件打开乱码，脚本会自动尝试UTF-8、GBK、Latin1编码。

### 2. Excel文件支持
需要安装`openpyxl`库：`pip install openpyxl`

### 3. 数量拆分
如果源数据中Quantity字段为小数，会先四舍五入取整再拆分。

### 4. 空值处理
所有空值会自动转换为空字符串，符合ShipStation导入要求。

## 版本历史

- **V7.0**: 尺寸优化版本，增加小于1的尺寸强制设为1的保底机制
- **V1.0**: 基础版本，实现基本字段映射和转换功能

## 相关资源

- [ShipStation官方导入指南](https://help.shipstation.com/hc/en-us/articles/360025856192-How-to-Import-Orders-into-ShipStation)
- [简道云数据导出教程](https://hc.jiandaoyun.com/doc/14305)