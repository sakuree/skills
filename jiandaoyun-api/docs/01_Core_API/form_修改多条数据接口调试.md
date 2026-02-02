# 修改多条数据接口调试

URL: https://hc.jiandaoyun.com/open/14225

## 1. 简介

### 1.1 接口简介

通过修改多条数据接口，可以批量修改多条数据。

注：

1）修改多条数据接口暂不支持子表单。

2）最多支持修改 100 条数据。

3）附件和图片字段更新时会清除字段中原有的文件。

4）修改多条数据是指把多条数据的字段修改成一个固定值。

### 1.2 接口版本说明

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2021.12.30 | 原始接口 |
| v5 | 2022.10.28 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 10 次/秒；  参数 app\_id 和 entry\_id 放入 body，接口路由修改为 POST app/entry/data/batch\_update。 |

## 2. 接口调用

批量更新多条数据。

**请求地址：**https://api.jiandaoyun.com/api/v5/app/entry/data/batch\_update

**请求频率**：10 次秒

**请求方式：**POST

**请求参数：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **类型** | **必需** | **说明** |
| app\_id | String | 是 | 应用ID |
| entry\_id | String | 是 | 表单ID |
| data\_ids | Array | 是 | 要更新的数据 ID 数组 |
| data | JSON | 是 | 数据内容，暂不支持子表单 |
| transaction\_id | String | 否 | 事务 ID；transaction\_id 用于绑定一批上传的文件，若数据中包含附件或图片控件，则 transaction\_id 必须与“[获取文件上传凭证和上传地址接口](https://hc.jiandaoyun.com/open/13287)”中的 transaction\_id 参数相同 |

**请求示例：**

```
{
  "app_id": "59264073a2a60c0c08e20bfb",
  "entry_id": "59264073a2a60c0c08e20bfd",
  "transaction_id": "87cd7d71-c6df-4281-9927-469094395677",   //事务ID
    "data_ids": [
        "200001181fe09728936510eb",
        "200001181fe09728936510ec",
        "200001181fe09728936510ed"
    ],
    "data": {
        "_widget_1432728651402": { // 单行文本
            "value": "简道云1"
        },
        "_widget_1432728651403": { // 数字
            "value": 100
        },
        "_widget_1725969783950": {
      		"value": "67221b4fac0a62ac8f43a1c4"//关联数据
    	}
    }
}
```

**响应内容：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| status | String | 返回请求结果 |
| success\_count | Number | 修改成功的数据条数 |

**响应示例：**

```
{
    "status": "success",
    "success_count": 3
}
```