# 查询单条数据接口调试

URL: https://hc.jiandaoyun.com/open/14221

## 1. 简介

### 1.1 接口简介

通过查询单条数据接口，可以查询表单中的指定数据。

### 1.2 接口版本说明

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2018.6.21 | 原始接口 |
| v2 | 2021.3.11 | 在 v2 的基础上，子表单新增数据 ID 参数，即为子表单中每条子数据新增一个数据 ID（以下简称数据 ID） |
| v3 | - | 无 v3 版本 |
| v4 | 2022.4.21 | 在 v3 的基础上，新增互联组织部门/成员获取，新增 type 参数类型：   * 0：内部 * 2：外部 |
| v5 | 2022.10.28 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；  参数 app\_id 和 entry\_id 放入 body，接口路由修改为 POST app/entry/data/get。 |

## 2. 接口调用

按照指定数据 ID 获取表单中的数据。

**请求地址**：https://api.jiandaoyun.com/api/v5/app/entry/data/get

**请求频率**：30 次/秒

**请求方式**：POST

**请求参数：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **类型** | **必需** | **说明** |
| app\_id | String | 是 | 应用ID |
| entry\_id | String | 是 | 表单ID |
| data\_id | String | 是 | 数据 ID |

**请求示例：**

```
{
   "app_id": "59264073a2a60c0c08e20bfb",
   "entry_id": "59264073a2a60c0c08e20bfd",
   "data_id": "59e9a2fe283ffa7c11b1ddbf"
}
```

**响应内容：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| data | JSON | 单条数据 |

**响应示例：**

```
{
    "data": {
        "_id": "59e9a2fe283ffa7c11b1ddbf",  
        "appId": "59264073a2a60c0c08e20bfb",
        "entryId": "59264073a2a60c0c08e20bfd",
        "creator": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "updater": {
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "createTime": "2017-10-20T22:41:51.430Z", // 创建时间
        "updateTime": "2017-10-20T11:12:15.293Z", // 修改时间
        "_widget_1725969783950": "67221b4fac0a62ac8f43a1c2",//关联数据
        "_widget_1432728651402": "简道云",  // 单行文本
        "_widget_1432728651403": 100, // 数字
        "_widget_1432728651404": "简道云是一个强大易用的应用搭建工具，可以快速把你的想法变成应用", // 多行文本
        "_widget_1432728651405": "选项一", // 单选按钮组、下拉框
        "_widget_1432728651406": [ // 复选框组、下拉复选框
            "选项一",
            "选项二",
            "选项三"
        ],
        "_widget_1432728651407": "2018-01-01T10:10:10.000Z", // 日期时间
        "_widget_1432728651408": { 
            "id": "5b28effa49b561455dfda91e"
        },// 选择数据
        "_widget_1432728651409": [ // 图片
            {
                "name": "image.jpg",
                "size": 262144,
                "mime": "image/jpeg",
                "url": "https://files.jiandaoyun.com/lepxaifzcapghupffcaswikmhnyp"
            }
        ],
        "_widget_1432728651410": [ // 附件
            {
                "name": "产品说明文档.pdf",
                "size": 524288,
                "mime": "application/pdf",
                "url": "https://files.jiandaoyun.com/bogrebbkdbkfsbuldnjujoenclle"
            }
        ],
        "_widget_1432728651411": { // 手写签名
            "name": "image.png",
            "size": 262144,
            "mime": "image/png",
            "url": "https://files.jiandaoyun.com/sxbikbrchwlylrgqwyfkjbjmuncp"
        },
        "_widget_1432728651412": { // 地址
            "province": "江苏省",
            "city": "无锡市",
            "district": "梁溪区",
            "detail": "清扬路138号茂业天地"
        },
        "_widget_1432728651413": { // 定位
            "province": "江苏省",
            "city": "无锡市",
            "district": "梁溪区",
            "detail": "清扬路138号茂业天地",
            "lnglatXY": [
                120.31237,
                31.49099
            ]
        },
        "_widget_1652345009097": { // 手机字段
            "verified": false,
            "phone": "15852540044"
        },
        "_widget_1432728651414": { // 成员单选
            "name": "小简",
            "username": "xiaojian",
            "status": 1,
            "type": 0,
            "departments": [1, 3],
            "integrate_id": "xiaojian"
        },
        "_widget_1432728651415": [ // 成员多选
            {
                "name": "小简",
                "username": "xiaojian",
                "status": 1,
                "type": 0,
                "departments": [1, 3],
                "integrate_id": "xiaojian"
            }
        ],
        "_widget_1432728651416": {  // 部门单选
            "name": "经理部",
            "dept_no": 1,
            "type": 0,
            "parent_no": 2,
            "status": 1,
            "integrate_id": 1
        },
        "_widget_1432728651417": [ // 部门多选
            {
                "name": "经理部",
                "dept_no": 1,
                "type": 0,
                "parent_no": 2,
                "status": 1,
                "integrate_id": 1
            }
        ],
        "_widget_1432728651408": [ // 子表单
            {
                // ... 同前面
            }
        ],
        "_widget_1432728651528": {
    		"html": "<p>Hello, world!<img src=\"https://files.xxxxxx.com/xxx\" /></p>",
    		"attachments": [
        		{
            		"name": "image1.png",
           			"size": 262144,
            		"mime": "image/png",
            		"url": "https://files.xxxxx.com/xxx"
        		}
    		]
		},
        "wx_open_id": "wx98fb14481b3ab5a3",
        "wx_nickname": "jiandaoyun",
        "wx_gender": "男"
    }
}
```