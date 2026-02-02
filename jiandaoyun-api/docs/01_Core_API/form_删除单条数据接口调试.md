# 删除单条数据接口调试

URL: https://hc.jiandaoyun.com/open/14226

## 1. 简介

### 1.1 接口简介

通过删除单条数据接口，可以对指定的数据进行删除。

### 1.2 接口版本说明

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2018.6.21 | 原始接口 |
| v5 | 2022.10.28 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；  参数 app\_id 和 entry\_id 放入 body，接口路由修改为 POST app/entry/data/delete。 |

## 2. 接口调用

按照指定数据 ID 从表单中删除数据。

**请求地址：**https://api.jiandaoyun.com/api/v5/app/entry/data/delete

**请求频率**：20 次/秒

**请求方式：**POST

**请求参数：**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **参数** | **类型** | **必需** | **说明** | **默认** |
| app\_id | String | 是 | 应用ID |  |
| entry\_id | String | 是 | 表单ID |  |
| data\_id | String | 是 | 数据 ID |  |
| is\_start\_trigger | Bool | 否 | 是否触发智能助手 | false |

**请求示例：**

```
{
    "app_id": "59264073a2a60c0c08e20bfb",
    "entry_id": "59264073a2a60c0c08e20bfd",
    "data_id": "6052e8072315c0075001d65e"
}
```

**响应内容：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| status | String | 返回请求结果 |

**响应示例：**

```
{
    "status": "success"
}
```