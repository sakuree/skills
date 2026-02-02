# 查询多条数据接口调试

URL: https://hc.jiandaoyun.com/open/14220

## 1. 简介

### 1.1 接口简介

通过查询多条数据接口，可以一次查询表单中的多条数据。

### 1.2 接口版本说明

|  |  |  |
| --- | --- | --- |
| **接口版本** | **更新时间** | **版本说明** |
| v1 | 2018.6.21 | 原始接口 |
| v2 | 2021.3.11 | 在 v2 的基础上，子表单新增数据 ID 参数，即为子表单中每条子数据新增一个数据 ID（以下简称数据 ID） |
| v3 | - | 无 v3 版本 |
| v4 | 2022.4.21 | 在 v3 的基础上，新增互联组织部门/成员获取，新增 type 参数类型：   * 0：内部 * 2：外部 |
| v5 | 2022.10.28 | 在 v4 的基础上，接口请求频率由 5 次/秒提升至 30 次/秒；  参数 app\_id 和 entry\_id 放入 body，接口路由修改为 POST app/entry/data/list。 |

## 2. 接口调用

该接口的返回数据，始终按照数据 ID 正序排列。

**请求地址**：https://api.jiandaoyun.com/api/v5/app/entry/data/list

**请求频率：**30 次/秒

**请求方式**：POST

**请求参数：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **类型** | **必需** | **说明** |
| app\_id | String | 是 | 应用ID |
| entry\_id | String | 是 | 表单ID |
| data\_id | String | 否 | 分页符，上一次查询数据结果的最后一条数据的 ID，没有则留空 |
| fields | Array | 否 | 需要查询的数据字段 |
| filter | JSON | 否 | 数据筛选器 |
| limit | Number | 否 | 查询的数据条数，1~100，默认10 |

### 数据筛选器

查询多条数据接口同时也支持过滤，可通过 filter 参数进行数据过滤。

**筛选结构：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **必需** | **类型** | **说明** |
| rel | 是 | String | 筛选组合关系；“and”(满足所有过滤条件), “or”(满足任一过滤条件) |
| cond | 是 | [JSON] | 过滤条件列表 |

**筛选示例：**

```
{
    "rel": "and", // 或者 "or"
    "cond": [
        // 过滤条件
    ]
}
```

**过滤条件结构：**

|  |  |  |  |
| --- | --- | --- | --- |
| **参数** | **必需** | **类型** | **说明** |
| field | 是 | String | 字段名 |
| type | 否 | String | 字段类型 |
| method | 是 | String | 过滤方法：   * not\_empty：不为空 * empty：为空 * eq：等于 * ne：不等于 * in：等于任意一个，最多可传递 200 个 * range：在 x 与 y 之间，并且包含 x 和 y 本身 * nin：不等于任意一个，最多可传递 200 个 * like：包含 * verified：表示填写了手机号且已验证的值 * unverified：表示填写了手机号但未验证值 * all：同时包含 * gt：大于 * lt：小于 |
| value | 否 | Array | 过滤值 |

**过滤条件示例：**

```
// 没有参数的过滤条件
{
    "field": "_widget_1508400000001",
    "type": "text",
    "method": "empty"
}
// 有参数的过滤条件
{
    "field": "flowState",
    "type": "flowstate",
    "method": "eq",
    "value": [1]
}
```

**目前支持如下字段：**

|  |  |  |
| --- | --- | --- |
| **字段类型** | **支持的过滤方式** | **说明** |
| flowState | eq，ne，in，nin，empty，not\_empty | 流程状态，仅对流程表单有效 |
| data\_id | eq， in， empty， not\_empty | 数据 id 字段，是数据唯一性的标识 |
| 提交人 | eq， ne， in， nin，empty，not\_empty | —— |
| 日期时间 | eq，ne，range，empty，not\_empty | 包含日期时间字段和提交时间字段 |
| 数字 | eq，ne，range，empty，not\_empty，gt，lt | —— |
| 文本 | eq，ne，in，nin，empty，not\_empty | 包括单行文本、下拉框、单选按钮组、流水号 |
| 复选框组/下拉复选框 | in，all，empty，not\_empty | —— |
| 手机 | like, verified, unverified, empty, not\_empty | verified表示填写了手机号且已验证的值；unverified表示填写了手机号但未验证值 |
| 流水号 | like，empty，not\_empty | —— |
| 关联数据 | eq，ne，in，nin，empty，not\_empty |
| 其他表单字段（子表单字段除外） | empty，not\_empty |

**请求示例：**

```
 {
    "app_id": "59264073a2a60c0c08e20bfb",
     "entry_id": "59264073a2a60c0c08e20bfd",
   "data_id": "59e9a2fe283ffa7c11b1ddbf", //此处 data_id 用于分页
    "limit": 100,
    "fields": ["_widget_1508400000001", "_widget_1508400000002", "_widget_1508400000003"],
    "filter": {
        "rel": "and", // 或者 "or"
        "cond": [
          {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"eq",//过滤方式为 eq
                "value":[0]
            } ,  
           {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"ne",//过滤方式为 ne
                "value":[0]
            } ,
           {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"in",//过滤方式为 in
                "value":[0,1]
            } ,
           {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"nin",//过滤方式为 nin
                "value":[0,1]
             } ,
            {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"empty",//过滤方式为 empty
             } ,
            {
                "field": "flowState",
                "type":"flowstate",//字段类型为 flowstate
                "method":"not_empty",//过滤方式为 not_empty
             } ,
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "range",//过滤方式为 range
                "value":["2024-11-20","2024-11-21"]
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "eq",//过滤方式为 eq
                "value":["2024-11-30"]
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "ne",//过滤方式为 ne
                "value":["2024-11-30"]
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "empty",//过滤方式为 empty
             },
            {
                "field": "_widget_1732071387201",
                "type": "datetime",//字段类型为 datetime
                "method": "not_empty",//过滤方式为 not_empty
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "eq",//过滤方式为 eq
                "value":[1]
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "ne",//过滤方式为 ne
                "value":[1]
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "range",//过滤方式为 range
                "value":[100,200]
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "empty",//过滤方式为 empty
             },
            {
                "field": "_widget_1732071387200",
                "type": "number",//字段类型为 number
                "method": "not_empty",//过滤方式为 not_empty
             },
            {
                "field": "_widget_1732071387201",
                "type": "number", //字段类型为 number
                "method": "gt", //过滤方式为 gt
                "value": [1000]
        	 },
            {
              "field": "_widget_1732071387202",
              "type": "number", //字段类型为 number
              "method": "lt", //过滤方式为 lt
              "value": [1000]
             },           
            {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "eq",//过滤方式为 eq
                "value":["111"]
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "ne",//过滤方式为 ne
                "value":["111"]
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "in",//过滤方式为 in
                "value":["111","2222"]
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "nin",//过滤方式为 nin
                "value":["111","2222"]
             },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "empty",//过滤方式为 empty
              },
             {
                "field": "_widget_1732071387199",
                "type": "text",//字段类型为 text
                "method": "not_empty",//过滤方式为 not_empty
             },
            {
                "field": "_widget_1732071387219",
                "type": "text", //字段类型为 text
                "method": "like", //过滤方式为 like
                "value": ["SN2024"]
             },
            {
                "field": "_widget_1732071387203",
                "type": "combocheck", //字段类型为 combocheck
                "method": "in", //过滤方式为 in
                "value": ["选项1", "选项2", "选项3"]
              },
             {
                "field": "_widget_1732071387204",
                "type": "combocheck", //字段类型为 combocheck
                "method": "all", //过滤方式为 all
                "value": ["选项A", "选项B"]
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "like",//过滤方式为 like
                "value":["188"]
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "verified",//过滤方式为 verified
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "unverified",//过滤方式为 unverified
             },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "empty",//过滤方式为 empty
              },
             {
                "field": "_widget_1732071387202",
                "type": "phone",//字段类型为 phone
                "method": "not_empty",//过滤方式为 not_empty
              },
            {
                "field": "_widget_1732071387220",
                "type": "lookup", //字段类型为 lookup
                "method": "eq", //过滤方式为 eq
                "value": ["507f1f77bcf86cd799439031"]
              },
            {
                "field": "_widget_1732071387221",
                "type": "lookup", //字段类型为 lookup
                "method": "ne", //过滤方式为 ne
                "value": ["507f1f77bcf86cd799439032"]
              },
            {
                "field": "_widget_1732071387222",
                "type": "lookup", //字段类型为 lookup
                "method": "in", //过滤方式为 in
                "value": ["507f1f77bcf86cd799439033", "507f1f77bcf86cd799439034"]
              },
             {
                "field": "_widget_1732071387223",
                "type": "lookup", //字段类型为 lookup
                "method": "nin", //过滤方式为 nin
                "value": ["507f1f77bcf86cd799439035", "507f1f77bcf86cd799439036"]
              },
             {
                "field": "_widget_1732071387224",
                "type": "lookup", //字段类型为 lookup
                "method": "empty", //过滤方式为 empty
              },
             {
                "field": "_widget_1732071387225",
                "type": "lookup", //字段类型为 lookup
                "method": "not_empty", //过滤方式为 not_empty
              },
             {
                "field": "data_id", //此处的 data_id 用筛选
                "type": "dataid",//字段类型为 dataid
                "method": "eq", //过滤方式为 eq
                "value": ["507f1f77bcf86cd799439037"]
              },
             {
                "field": "data_id", //此处的 data_id 用筛选
                "type": "dataid", //字段类型为 dataid
                "method": "in", //过滤方式为 in
                "value": ["507f1f77bcf86cd799439038", "507f1f77bcf86cd799439039", "507f1f77bcf86cd799439040"]
              },
             {
                "field": "data_id", //此处的 data_id 用筛选
                "type": "dataid", //字段类型为 dataid
                "method": "empty", //过滤方式为 empty
              },
             {
                "field": "data_id",
                "type": "dataid", //字段类型为 dataid
                "method": "not_empty",//过滤方式为 not_empty
              },
             {
                "field": "creator", //此处的 data_id 用筛选
                "type": "user", //字段类型为 user
                "method": "eq", //过滤方式为 eq
                "value": ["507f1f77bcf86cd799439041"]
              },
             {
                "field": "creator",
                "type": "user", //字段类型为 user
                "method": "ne", //过滤方式为 ne
                "value": ["507f1f77bcf86cd799439042"]
              },
             {
                "field": "creator",
                "type": "user", //字段类型为 user
                "method": "in", //过滤方式为 in
                "value": ["507f1f77bcf86cd799439043", "507f1f77bcf86cd799439044"]
              },
             {
                "field": "creator",
                "type": "user", //字段类型为 user
                "method": "nin", //过滤方式为 nin
                "value": ["507f1f77bcf86cd799439045", "507f1f77bcf86cd799439046"]
              }
        ]
    }
}
```

**响应参数：**

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| data | Array | 多条数据的集合 |

**响应数据样例：**

```
{
    "data": [{
            "_id": "59e9a2fe283ffa7c11b1ddbe",
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
            "createTime": "2017-10-20T22:41:51.430Z",
            "updateTime": "2017-10-20T11:12:15.293Z",
   			"_widget_1741589364098": {
        			"id": "67ce8c18705dfcd1eef5c070"
      		},//选择数据字段
            "_widget_1432728651402": "A班",
            "_widget_1615777739673": [{
                    "_id": "604ed0298e2ade077c7245f1",
                    "_widget_1615777739744": "子表单数据1"
                },
                {
                    "_id": "604ed0298e2ade077c7245f2",
                    "_widget_1615777739744": "子表单数据2"
                }
            ]
        },
        {
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
            "createTime": "2017-10-20T22:41:51.430Z",
            "updateTime": "2017-10-20T11:12:15.293Z",
            "_widget_1725969783950": "67221b4fac0a62ac8f43a1c2",//关联数据字段
            "_widget_1741589364098": {
        			"id": "67ce8c18705dfcd1eef5c070"
      		},//选择数据字段
            "_widget_1432728651402": "B班",
            "_widget_1615777739673": [{
                    "_id": "604ed0298e2ade077c7245f3",
                    "_widget_1615777739744": "子表单数据1"
                },
                {
                    "_id": "604ed0298e2ade077c7245f4",
                    "_widget_1615777739744": "子表单数据2"
                }
            ]
        }
    ]
}
```

## 3. 注意事项

若要设置循环调取数据，可以利用 data\_id 字段来设置参数避免调取重复数据。

如需要查询 230 条数据：

* 第一次查询时可以不传 data\_id 字段，若设置 limit 为 100 ，则第一次返回了前 100 条数据；
* 第二次，用第 100 条数据的 data\_id 进行查询，若设置 limit 为100，则第二次返回 101～200 这 100 条数据；
* 第三次，用第 200 条数据的 data\_id 进行查询，若设置 limit 为100，则第三次返回 201～230 这 30 条数据。

由于第三次返回结果只有 30 条，未达到设置的 limit 上限100，则说明查询结束。

###