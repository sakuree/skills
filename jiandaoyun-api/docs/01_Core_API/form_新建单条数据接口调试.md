# 新建单条数据接口调试

URL: https://hc.jiandaoyun.com/open/14222

## 1. 简介

### 1.1 接口简介

通过新建单条数据接口，可以向指定的表单中添加单条数据。

注：使用 API 添加数据时，会触发的事件有新数据提交提醒、聚合表计算&校验、数据操作日志、数据量统计。也可以通过请求参数来控制是否发起流程。但是不会触发重复值校验、必填校验。

另外，[系统字段](https://hc.jiandaoyun.com/doc/13523) 和以下所列举的字段不支持添加和修改数据：

* 分割线
* 手写签名
* 选择数据、查询
* 流水号（提交后系统生成）

### 1.2 接口版本说明

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2018.6.21 | 部门和成员均使用\_id为主键 |
| v2 | 2019.6.21 | 在 v1 的基础上，成员字段使用 username 为主键，部门字段使用 dept\_no 为主键 |
| v3 | 2021.3.31 | 在 v2 的基础上，子表单新增数据 ID 参数，即为子表单中每条子数据新增一个数据 ID |
| v4 | 2022.4.21 | 在 v3 的基础上，新增互联组织部门/成员获取，新增 type 参数类型：   * 0：内部 * 2：外部 |
| v5 | 2022.10.28 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 20 次/秒；  参数 app\_id 和 entry\_id 放入 body，接口路由修改为 POST app/entry/data/create。 |
| 2023.08.31 | 新增请求参数，数据提交人：data\_creator |

## 2. 接口调用

在指定表单中添加一条数据。

**请求地址**：https://api.jiandaoyun.com/api/v5/app/entry/data/create

**请求频率：**20 次/秒

**请求方式**：POST

**请求参数：**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **参数** | **类型** | **必需** | **说明** | **默认** |
| app\_id | String | 是 | 应用ID |  |
| entry\_id | String | 是 | 表单ID |  |
| data | JSON | 是 | 数据内容 |  |
| data\_creator | String | 否 | 数据提交人（取成员编号 username，可从通讯录接口获取） | 企业创建者 |
| is\_start\_workflow | Bool | 否 | 是否发起流程（仅流程表单有效） | false |
| is\_start\_trigger | Bool | 否 | 是否触发智能助手 | false |
| transaction\_id | String | 否 | 事务ID；transaction\_id 用于绑定一批上传的文件，若数据中包含附件或图片控件，则 transaction\_id 必须与“[获取文件上传凭证和上传地址接口](https://hc.jiandaoyun.com/open/13287)”中的 transaction\_id 参数相同。 |  |

**请求示例：**

```
{
    "app_id": "59264073a2a60c0c08e20bfb",
    "entry_id": "59264073a2a60c0c08e20bfd",
    "transaction_id": "87cd7d71-c6df-4281-9927-469094395677",   //事务ID
    "data_creator":"Yonne",      //数据提交人
     "data": {
        "_widget_1432728651402": { // 单行文本
            "value": "简道云"
        },
          "_widget_1725969783950": {
      		"value": "67221b4fac0a62ac8f43a1c3"//关联数据字段ID
    	},
        "_widget_1432728651403": { // 数字
            "value": 100
        },
        "_widget_1432728651404": { // 多行文本
            "value": "简道云是一个强大易用的应用搭建工具，\n可以快速把你的想法变成应用"
        },
        "_widget_1432728651405": { // 单选按钮组、下拉框
            "value": "选项一"
        },
        "_widget_1432728651406": { // 复选框组、下拉复选框
            "value": [
                "选项一","选项二","选项三"
            ]
        },
        "_widget_1432728651407": { // 日期时间
            "value": "2018-01-01T10:10:10.000Z"
        },
        "_widget_1432728651412": {  // 地址
            "value": {
                "province": "江苏省",
                "city": "无锡市",
                "district": "梁溪区",
                "detail": "清扬路138号茂业天地"
            }
        },
        "_widget_1432728651413": { // 定位
            "value": {
                "province": "江苏省",
                "city": "无锡市",
                "district": "梁溪区",
                "detail": "清扬路138号茂业天地",
                "lnglatXY": [
                    120.31237,
                    31.49099
                ]
            }
        },
        "_widget_1528854613291": { // 子表单
            "value": [
                { // 子表单子记录结构跟主表一致
                    "_widget_1528854614409": {
                        "value": "子表单数据1"
                    },
                    "_widget_1528854615499": {
                        "value": 1001
                    }
                },
                {
                    "_widget_1528854614410": {
                        "value": "子表单数据2"
                    },
                    "_widget_1528854615419": {
                        "value": 1002
                    }
                }
            ]
        },
        "_widget_1652345009097": { //手机字段
            "value": {
                "phone": "15852540044"
            }
        },
        "_widget_1652345009126": { //成员单选（成员的username）
            "value": "jian"
        },
        "_widget_1652345009143": { //成员多选（成员的username数组）
            "value": [
                "jian",
                "dao"
            ]
        },
        "_widget_1652345009157": { //部门单选（部门的dept_no）
            "value": 12
        },
        "_widget_1652345009174": { //部门多选（部门的dept_no数组）
            "value": [
                12,
                13
            ]
        },
        "_widget_1432728651408": { // 附件（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-8fa8fdeae2ef","6b559cf1-b16c-43bd-a211-646ab85da8cb"]
        },
        "_widget_1432728652567": { // 图片（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-74389cd8ae76","6b559cf1-b16c-43bd-a211-564e56a65bd6"]
        },
        "_widget_1432728651408": { // 附件（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-8fa8fdeae2ef","6b559cf1-b16c-43bd-a211-646ab85da8cb"]
        },
        "_widget_1432728652567": { // 图片（文件key数组）
            "value": ["6b559cf1-b16c-43bd-a211-74389cd8ae76","6b559cf1-b16c-43bd-a211-564e56a65bd6"]
        },
        "_widget_1432728651528": { // 富文本（img标签中的data-key是文件key）
    		"value": "<p>Hello, world!<img data-key=\"6b559cf1-b16c-43bd-a211-74389cd8ae76\" width=\"100\" height=\"100\" /></p>"
		}
    }
}
```

**响应内容：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| data | JSON | 返回提交后的完整数据，内容同查询单条数据接口 |

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
        "_widget_1432728651402": "简道云",  // 单行文本
        "_widget_1725969783950": "67221b4fac0a62ac8f43a1c3",//关联数据
        "_widget_1432728651403": 100, // 数字
        "_widget_1432728651404": "简道云是一个强大易用的应用搭建工具，可以快速把你的想法变成应用", // 多行文本
        "_widget_1432728651405": "选项一", // 单选按钮组、下拉框
        "_widget_1432728651406": [ // 复选框组、下拉复选框
            "选项一、选项二、选项三"
        ],
        "_widget_1432728651407": "2018-01-01T10:10:10.000Z", // 日期时间
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

## 3. 注意事项

如果请求中指定了 data\_creator，则关联触发的以下成员也会被记录为 data\_creator，如下所示：

* 智能助手执行人
* 流程发起人
* CRM 相关关联修改

+ 由跟进记录关联修改的客户表、线索表和商机表的修改人
+ 由商机表关联修改的客户表的修改人