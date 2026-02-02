# 删除多条数据接口调试

URL: https://hc.jiandaoyun.com/open/14527

## 1. 简介

### 1.1 接口简介

通过删除多条数据接口，可以批量删除数据。

> 删除多条数据接口一次最多支持删除 100 条数据。

### 1.2 接口版本说明

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2022.6.14 | 原始接口 |
| v5 | 2022.10.28 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；  参数 app\_id 和 entry\_id 放入 body，接口路由修改为 POST app/entry/data/batch\_delete。 |

## 2. 接口调用

按照指定数据 ID 批量从表单中删除数据。

**请求地址：**https://api.jiandaoyun.com/api/v5/app/entry/data/batch\_delete

**请求频率：**10 次/秒

**请求方式：**POST

**请求参数：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **必须** | **类型** | **说明** |
| app\_id | 是 | String | 应用ID |
| entry\_id | 是 | String | 表单ID |
| data\_ids | 是 | String[] | 要删除的数据ID数组 |

**请求示例：**

```
{
    "app_id": "59264073a2a60c0c08e20bfb",
    "entry_id": "59264073a2a60c0c08e20bfd",
    "data_ids": [
        "200001181fe09728936510eb",
        "200001181fe09728936510ec",
        "200001181fe09728936510ed"
    ]
}
```

**响应参数：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| status | String | 成功返回‘success’ |
| success\_count | number | 删除成功的数据条数 |

**响应示例：**

```
{  
    "status": "success",
    "success_count": 3
}
```