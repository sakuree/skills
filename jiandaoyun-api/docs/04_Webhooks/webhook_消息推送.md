# 消息推送

URL: https://hc.jiandaoyun.com/open/11497

## 1. 功能简介

消息推送可以将简道云中的待办通知、消息通知、抄送通知等消息同步到自己的服务器，便于企业的业务整合。

## 2. 推送服务器配置方法

### 2.1 配置入口

点击右上角头像，进入「企业管理 >>消息推送」，开启消息推送的开关：

![](https://help-assets.jiandaoyun.com/71745592-5839-48d0-84bf-11f12f70d743)

### **2.2 服务器配置**

点击「配置」，进入消息推送的配置页面，填写服务器地址后，可通过「服务器连接测试」测试连接是否成功，点击「生成 Secret」，即可自动生成消息推送的 Secret，设置好后点击「保存」：

![](https://help-assets.jiandaoyun.com/1b074aba-624d-4fc1-8454-d93fa59e2066)

## 3. 推送数据结构说明

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | 推送事件 |
| data | json | 推送内容 |
| send\_time | string | 推送时间 |

数据样例如下：

```
{
    op: "flow_message", //推送事件
    data: {
        to: [{
            username: "jiandaoyun",
            name: "小云"    
        }],
        entry_name: "请假审批",
        notify_text: "小云本周五请假1天",
        url: "https://abc.com/xyz"
    }, //推送内容
    send_time: "2017-10-20T22:41:51.430Z" //推送时间
}
```

## 4. 推送事件

### 4.1 表单自定义时间提醒

#### **4.1.1 配置方式**

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「自定义时间提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

![](https://help-assets.jiandaoyun.com/0f1659f8-2c0e-4821-b8ed-82e622ea1d6d)

#### **4.1.2 推送内容**

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | “form\_schedule\_message”，固定值 |
| data | json | 推送内容 |
| data.to | json[] | 被提醒人列表 |
| data.entry\_name | string | 推送来源表单名称 |
| data.notify\_text | string | 提醒文字，默认为“已到提醒时间，请及时处理”，可在提醒设置中自定义 |
| data.url | string | 表单内链，需表单授权才可访问 |
| send\_time | string | 推送时间 |

#### **4.1.3 推送数据样例**

```
{
	op: "form_schedule_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}, {
				username: "dao",
				name: "小道"
			}
		],
		entry_name: "请假审批",
		notify_text: "小云提出请假申请，请审批",
		url: "https://jiandaoyun.com/app/1/entry/2"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}
```

### 4.2 表单新数据提交提醒

#### **4.2.1 配置方式**

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「新数据提交时提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

![](https://help-assets.jiandaoyun.com/1757e24f-052c-48e9-af2c-329a50267e13)

#### **4.2.2 推送内容**

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | “data\_create\_message”，固定值 |
| data | json | 推送内容 |
| data.to | json[] | 被提醒人列表 |
| data.entry\_name | string | 推送来源表单名称 |
| data.notify\_text | string | 提醒文字，默认为“有新数据提交，请及时处理”，可在提醒设置中自定义 |
| data.content | string | 详细内容，有值的表单字段标题和字段值。例如：“单行文本: 123\n多行文本: 1233\n数字: 123\n成员单选: codingmagic1\n部门单选: 研发\n日期时间: 2019-06-13” |
| data.url | string | 静态消息链接，属于被提醒人的个人消息，登录后可访问 |
| send\_time | string | 推送时间 |

#### **4.2.3 推送数据样例**

```
{
	op: "data_create_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}, {
				username: "dao",
				name: "小道"
			}
		],
		entry_name: "请假审批",
		notify_text: "小云提出请假申请，请审批",
		content: "请假人: 小云\n请假原因: 病假",
		url: "https://jiandaoyun.com/message/1/data"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}
```

### 4.3 表单数据修改后提醒

#### **4.3.1 配置方式**

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「数据修改后提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

![](https://help-assets.jiandaoyun.com/2e4bbcfc-6dc7-44e7-a887-c76828c67ce3)

#### **4.3.2 推送内容**

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | “data\_update\_message”，固定值 |
| data | json | 推送内容 |
| data.to | json[] | 被提醒人列表 |
| data.entry\_name | string | 推送来源表单名称 |
| data.notify\_text | string | 提醒文字，默认为“有数据被修改，请及时处理”，可在提醒设置中自定义 |
| data.content | string | 详细内容，修改人、数据标题、被修改的字段。例如：“修改人: test\_li\n数据标题: 1231\n单行文本: 123→1231\n成员单选: codingmagic1→codingjun” |
| data.url | string | 数据内链，需表单授权才可访问 |
| send\_time | string | 推送时间 |

#### **4.3.3 推送数据样例**

```
{
	op: "data_update_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "请假审批",
		notify_text: "小云修改了请假日期",
		content: "修改人: 小云\n数据标题: 病假申请\n请假日期: 2018-5-1→2018-5-2",
		url: "https://jiandaoyun.com/dashboard/app/1/form/2/data/3/qr_link"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}
```

### 4.4 根据表单内日期时间字段提醒

#### **4.4.1 配置方式**

进入表单「扩展功能 >> 推送提醒」，点击「新建推送提醒」，填写好「根据表单内日期时间字段提醒」的提醒内容，在提醒方式处勾选「推送至我的服务器」：

![](https://help-assets.jiandaoyun.com/d239900b-a3c1-4e84-b934-7192887ced7a)

#### **4.4.2 推送内容**

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | “form\_widget\_message”，固定值 |
| data | json | 推送内容 |
| data.to | json[] | 被提醒人列表 |
| data.entry\_name | string | 推送来源表单名称 |
| data.notify\_text | string | 提醒文字，默认为“有数据到期，请及时处理”，可在提醒设置中自定义 |
| data.content | string | 详细内容，数据标题 |
| data.url | string | 数据内链，单表单超出 10 条后发送表单内链，需表单授权才可访问 |
| send\_time | string | 推送时间 |

#### **4.4.3 推送数据样例**

```
{
	op: "form_widget_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "生日提醒",
		notify_text: "小云的生日到了",
		content: "小云的生日到了",
		url: "https://jiandaoyun.com/dashboard/app/1/form/2/data/3/qr_link"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}
```

### 4.5 表单流程消息提醒

当流程发起、抄送、转交、回退、超时、激活、调整负责人时，都会给当前流程负责人推送流程提醒信息。

#### **4.5.1 配置方式**

进入流程表单的「流程设定」，在「流程属性 >> 流程提醒」处勾选「推送至我的服务器」：

![](https://help-assets.jiandaoyun.com/edafe1de-5a96-464f-b522-ca01652eb507)

#### **4.5.2 推送内容**

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | “flow\_message”，固定值 |
| data | json | 推送内容 |
| data.flow\_action | string | 流程操作 |
| data.to | json[] | 被提醒人列表 |
| data.entry\_name | string | 推送来源表单名称 |
| data.notify\_text | string | 提醒文字，默认为“有数据被修改，请及时处理” |
| data.content | string | 详细内容，流程简报 |
| data.url | string | 数据内链，需表单授权才可访问 |
| send\_time | string | 推送时间 |

不同的流程操作（flow\_action）对应不同的推送内容，具体如下表所示：

|  |  |  |  |
| --- | --- | --- | --- |
| **流程操作** | **含义** | **提醒文字** | **详细内容** |
| flow\_forward | 提交 | 有新的流程待办事项 | 流程简报，例如：“单行文本: 123\n多行文本: 123\n数字: 123” |
| flow\_auto\_forward | 系统自动提交 | 有新的流程待办事项 | 同上 |
| flow\_back | 回退 | 提交的流程事项被回退 | 同上 |
| flow\_auto\_back | 系统自动回退 | 提交的流程事项被回退 | 同上 |
| flow\_cc | 抄送 | 有新的流程处理结果抄送给您 | 同上 |
| flow\_timeout | 流程超时 | 默认为“有待办未完成，请及时处理”，可在超时提醒设置中自定义 | 同上 |
| flow\_member\_transfer | 成员转交 | 由「~$转交人」转交给您1条待办事项 | 同上 |
| flow\_admin\_transfer | 一条流程数据被管理员调整负责人 | 由系统管理员转交给您1条待办事项 | 同上 |
| flow\_activate | 流程被激活 | 由系统管理员转交给您1条待办事项 | 同上 |
| flow\_sign\_before | 前加签 | 由「~$加签人」加签给您1条待办事项 | 同上 |
| flow\_sign\_after | 后加签 | 由「~$加签人」加签给您1条待办事项 | 同上 |
| flow\_sign\_parallel | 添加审批人 | 由「~$加签人」加签给您1条待办事项 | 同上 |
| flow\_sign\_before\_complete | 前加签处理完成 | 前加签处理已完成，您有新的流程待办事项 | 同上 |
| flow\_batch\_transfer | 多条流程数据被管理员调整负责人 | 由系统管理员转交给您新的待办事项 | 无 |
| flow\_batch\_forward | 多条流程提交 | 有[~$count]条新的流程待办事项 | 无 |
| flow\_batch\_cc | 多条流程抄送 | 有[~$count]条新的流程处理结果抄送给您 | 无 |
| flow\_urge | 流程催办 | 有一条流程急需处理 | 无 |

#### **4.5.3 新旧流程消息推送时变化**

**1）新旧流程消息推送时to的变化**

* 旧版to：会集合在同一条推送里，见下方代码中的 **to 部分**，无论节点多少人，就只推送一次。

```
{
    "data": {
      "content": "",
      "entry_name": "旧版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "张三",
          "username": "zhangsan"
        },
        {
          "name": "李四",
          "username": "lisi"
        },
        {
          "name": "王五",
          "username": "wangwu"
        }
      ],
      "url": "https://www.jiandaoyun.com/dashboard/app/642e37f2374e1b0007f537b2/form/642e37f5fe736900073a99e5/data/642e3855dd27960007cf9514?actionType=flow_forward&flowId=1&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:11:18.102Z"
}
```

* 新版to：会拆分为多条推送，有几个负责人就推送几条，如下该节点有三个负责人，则推送三次，to 里面始终只有一个人。

```
{
    "data": {
      "content": "",
      "entry_name": "新版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "张三",
          "username": "zhangsan"
        }
      ],
      "url": "https://www.jiandaoyun.com/message/redirect?msg=task_inst%3A%3A%3A%3A%3A&instanceId=642e38acd039d000080c637b&taskId=642e38acd039d000080c63a3&actionType=flow_forward&appId=63b62c3d0c76a3000a0bf8a6&dataId=642e38acd039d000080c637b&flowId=3&formId=63b62c3fa76046000a36d412&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:12:44.991Z"
}

{
    "data": {
      "content": "",
      "entry_name": "新版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "李四",
          "username": "lisi"
        }
      ],
      "url": "https://www.jiandaoyun.com/message/redirect?msg=task_inst%3A%3A%3A%3A%3A&instanceId=642e38acd039d000080c637b&taskId=642e38acd039d000080c63a3&actionType=flow_forward&appId=63b62c3d0c76a3000a0bf8a6&dataId=642e38acd039d000080c637b&flowId=3&formId=63b62c3fa76046000a36d412&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:12:44.991Z"
}

{
    "data": {
      "content": "",
      "entry_name": "新版流程推送测试",
      "flow_action": "flow_forward",
      "notify_text": "有新的流程待办事项",
      "to": [
        {
          "name": "王五",
          "username": "wangwu"
        }
      ],
      "url": "https://www.jiandaoyun.com/message/redirect?msg=task_inst%3A%3A%3A%3A%3A&instanceId=642e38acd039d000080c637b&taskId=642e38acd039d000080c63a3&actionType=flow_forward&appId=63b62c3d0c76a3000a0bf8a6&dataId=642e38acd039d000080c637b&flowId=3&formId=63b62c3fa76046000a36d412&memberType=0&guestCorpId="
    },
    "op": "flow_message",
    "send_time": "2023-04-06T03:12:44.991Z"
}
```

**1）新旧流程消息推送时url的变化**

* 旧版地址：https://www.jiandaoyun.com/dashboard/app/6331609e3c17350008d45fdb/form/633160a368ae71000a94676a/data/64054250c68b1e0008b822a7?actionType=flow\_forward&flowId=1&memberType=0&guestCorpId=
* 新版地址：https://www.jiandaoyun.com/message/redirect?msg=task\_inst%3A%3A%3A%3A%3A&instanceId=64100d6e2ac023000782ec79&taskId=641b2fdec3ddb00007aa36a8&actionType=flow\_forward&flowId=1&memberType=0&guestCorpId=&appId=6331609e3c17350008d45fdb&formId=633160a368ae71000a94676a&dataId=64054250c68b1e0008b822a7

新版地址相较旧版地址差别如下所示：

* 数据 id 以 url 参数形式放在 url 中，参数名 instanceId 和 dataId 均等于数据 id；
* 应用 id 和表单 id 以 url 参数形式放在 url 中，参数名为 appId 和 formId；
* 新增了 taskId（任务 id，同一个节点多个负责人每个人的 taskId 不同）。

### 4.6 仪表盘定时提醒

#### **4.6.1 配置方式**

进入仪表盘的「仪表盘设计」，点击设置「定时提醒」，设置好提醒内容后，在提醒方式处勾选「推送至我的服务器」：

![](https://help-assets.jiandaoyun.com/68376055-4e48-4073-97d4-4a6a97767689)

#### **4.6.2 推送内容**

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | “dash\_schedule\_message”，固定值 |
| data | json | 推送内容 |
| data.to | json[] | 被提醒人列表 |
| data.entry\_name | string | 推送来源仪表盘名称 |
| data.notify\_text | string | 提醒文字，默认为“已到提醒时间，请及时处理”，可在提醒设置中自定义 |
| data.url | string | 仪表盘访问内链，需授权才可访问 |
| send\_time | string | 推送时间 |

#### **4.6.3 推送数据样例**

```
{
	op: "dash_schedule_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "物料盘点",
		notify_text: "2019年度物料盘点的时间到了",
		url: "https://jiandaoyun.com/app/1/entry/2"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}
```

### 4.7 仪表盘预警提醒

#### **4.7.1 配置方式**

进入统计表的编辑页面，在「功能配置 >> 数据预警」处添加预警，设置好预警内容后，在提醒方式处勾选「推送至我的服务器」：

![](https://help-assets.jiandaoyun.com/696d16b0-5fe0-46ca-a0e8-90bbabc758aa)

#### **4.7.2 推送内容**

|  |  |  |
| --- | --- | --- |
| **字段** | **类型** | **说明** |
| op | string | “dash\_alert\_message”，固定值 |
| data | json | 推送内容 |
| data.to | json[] | 被提醒人列表 |
| data.entry\_name | string | 推送来源仪表盘名称 |
| data.notify\_text | string | 使用预警名称作为提醒文字 |
| data.content | string | 详细内容，预警来源：{应用名称}>{仪表盘名称}>{组件名称} |
| data.url | string | 仪表盘内链，需仪表盘授权才可访问 |
| send\_time | string | 推送时间 |

#### **4.7.3 推送数据样例**

```
{
	op: "dash_alert_message",
	data: {
		to: [
			{
				username: "jian",
				name: "小简"
			}
		],
		entry_name: "库存统计",
		notify_text: "库存警告",
		content: "预警来源：库存应用>华南区盘点>库存剩余量",
		url: "https://jiandaoyun.com/app/1/entry/2"
	},
	send_time: "2017-10-20T22:41:51.430Z"
}
```