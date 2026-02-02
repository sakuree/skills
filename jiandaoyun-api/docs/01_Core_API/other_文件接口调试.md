# 文件接口调试

URL: https://hc.jiandaoyun.com/open/13287

## 1. 开发准备

开发前，请仔细阅读 [开发指南](/open/11261)。

## 2. 文件API

### 2.1 获取文件上传凭证和上传地址接口

获取文件上传凭证和上传地址接口

**接口版本说明：**

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2021.12.30 | 原始接口 |
| v5 | 2022.10.28 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；  参数 app\_id 和 entry\_id 放入 body，接口路由修改为 POST app/entry/file/get\_upload\_token。 |

**请求地址：**https://api.jiandaoyun.com/api/v5/app/entry/file/get\_upload\_token

**请求频率：** 20 次/秒

**请求方式：**POST

**接口说明：**

每次请求会获取 100 个文件上传凭证和上传地址，上传的文件会与 transaction\_id 绑定，只有相同 transaction\_id 的创建或修改请求才能使用该文件。

**请求参数：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **类型** | **必需** | **说明** |
| app\_id | String | 是 | 应用ID |
| entry\_id | String | 是 | 表单ID |
| transaction\_id | String | 是 | 事务ID |

注：

1）transaction\_id 参数需用户自己生成，推荐使用 UUID 格式。

2）transaction\_id 中，**不允许**包含 ${var}、$(var)、$(var}、${var) 模式的文本，否则将无法通过格式校验，导致接口调用失败。

**请求数据样例：**

```
{
 "app_id": "59264073a2a60c0c08e20bfb",
  "entry_id": "59264073a2a60c0c08e20bfd",
  "transaction_id": "87cd7d71-c6df-4281-9927-469094395677"   //事务ID
}
```

**响应内容：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| token\_and\_url\_list | JSON | 文件上传凭证和上传地址 |
| token\_and\_url\_list[].url | String | 文件上传地址 |
| token\_and\_url\_list[].token | String | 文件上传凭证 |

**响应示例：**

```
{
    "token_and_url_list": [
        {
            "url": "https://upload.qiniup.com",
            "token": "bM7UwVPyBBdPaleBZt21SWKzMy2qPUpn-05jZlas:ELIqACNut-t52UMPD-DZNrX8hTU=:eyJmc2l6ZU1pbiI6MSwiZnNpemVMaW1pdCI6MjA5NzE1MjAwLCJjYWxsYmFja0JvZHlUeXBlIjoiYXBwbGljYXRpb24vanNvbiIsImNhbGxiYWNrQm9keSI6IntcImFwcElkXCI6XCI2MWFjNzcxNTE0MjU3NDM2ODhlZWMwYzRcIixcImVudHJ5SWRcIjpcIjYxYWM3NzNhMTQyNTc0MzY4OGVlYzBjN1wiLFwia2V5XCI6XCIkKGtleSlcIixcImhhc2hcIjpcIiQoZXRhZylcIixcIm5hbWVcIjpcIiQoZm5hbWUpXCIsXCJzaXplXCI6XCIkKGZzaXplKVwiLFwibWltZVwiOlwiJChtaW1lVHlwZSlcIixcImJ1Y2tldFwiOlwiamR5LWZpbGVcIixcInVwbG9hZGVyXCI6XCI2MTFhMmQzNjRmMzQ3MDAwMDY3NWM5ZGRcIixcInNlc3Npb25JZFwiOlwic3NkXCJ9IiwiY2FsbGJhY2tIb3N0IjoiNTA3NS0xMTQtMjI0LTE3LTIxNi5uZ3Jvay5pbyIsImNhbGxiYWNrVXJsIjoiaHR0cDovLzUwNzUtMTE0LTIyNC0xNy0yMTYubmdyb2suaW8vZmlsZS91cGxvYWQvYXBpX2NhbGxiYWNrIiwiZm9yY2VTYXZlS2V5Ijp0cnVlLCJzYXZlS2V5IjoiYTJjOTkwY2ItMTlhZS00NDgwLTkyYzYtZDI3N2I5ZGQ2MmFhIiwic2NvcGUiOiJkbi1qZHktdXBsb2FkIiwiZGVhZGxpbmUiOjE2Mzk0ODU2NjV9"
        },
        {
            "url": "https://upload.qiniup.com",
            "token": "bM7UwVPyBBdPaleBZt21SWKzMylqPUpn-05jZlas:inKpUPPCKIWJ6CnZzHrRPnjXwio=:eyJmc226ZU1pbiI6MSwiZnNpemVMaW1pdCI6MjA5NzE1MjAwLCJjYWxsYmFja0JvZHlUeXBlIjoiYXBwbGljYXRpb24vanNvbiIsImNhbGxiYWNrQm9keSI6IntcImFwcElkXCI6XCI2MWFjNzcxNTE0MjU3NDM2ODhlZWMwYzRcIixcImVudHJ5SWRcIjpcIjYxYWM3NzNhMTQyNTc0MzY4OGVlYzBjN1wiLFwia2V5XCI6XCIkKGtleSlcIixcImhhc2hcIjpcIiQoZXRhZylcIixcIm5hbWVcIjpcIiQoZm5hbWUpXCIsXCJzaXplXCI6XCIkKGZzaXplKVwiLFwibWltZVwiOlwiJChtaW1lVHlwZSlcIixcImJ1Y2tldFwiOlwiamR5LWZpbGVcIixcInVwbG9hZGVyXCI6XCI2MTFhMmQzNjRmMzQ3MDAwMDY3NWM5ZGRcIixcInNlc3Npb25JZFwiOlwic3NkXCJ9IiwiY2FsbGJhY2tIb3N0IjoiNTA3NS0xMTQtMjI0LTE3LTIxNi5uZ3Jvay5pbyIsImNhbGxiYWNrVXJsIjoiaHR0cDovLzUwNzUtMTE0LTIyNC0xNy0yMTYubmdyb2suaW8vZmlsZS91cGxvYWQvYXBpX2NhbGxiYWNrIiwiZm9yY2VTYXZlS2V5Ijp0cnVlLCJzYXZlS2V5IjoiN2Y4Yzk3NDAtNmI2YS00OTQ0LWE0MzgtNjQ1Y2IzN2ViNmQ0Iiwic2NvcGUiOiJkbi1qZHktdXBsb2FkIiwiZGVhZGxpbmUiOjE2Mzk0ODU2NjV9"
        },
        ……
    ]
}
```

### 2.2 文件上传接口

用于上传文件的接口。

**接口版本说明：**

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2021.12.30 | 原始接口 |
| v5 | 2022.10.28 | 在 v1 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒 |

**请求地址：**{url}

**请求频率：** 20 次/秒

**请求方式：**POST

**接口说明：**

此处的 url 为获取文件上传凭证和上传地址接口中获取到的上传地址。

该接口一个 token 只能上传一个文件，不允许覆盖，返回的 key 用于创建和修改接口填写在附件或图片控件值中。

**请求参数：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **必需** | **类型** | **说明** |
| token | 是 | String | 文件上传凭证 |
| file | 是 | 文件 | 要上传的文件 |

注：

1）由于请求中需要上传文件，所以参数为 form-data 形式。

2）file 需要作为最后一个参数。

**响应内容：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| key | String | 文件key |

**响应数据样例：**

```
{
    "key": "6b559cf1-b16c-43bd-a211-8fa8fdeae2ef"
}
```

## 3. 注意事项

1. token 的有效时间为 1 小时。

2. transaction\_id 和 key 配合使用，transaction\_id 有效时间也为 1 小时，失效后，key 也将无法使用。