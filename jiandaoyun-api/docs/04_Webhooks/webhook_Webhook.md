# Webhook

URL: https://hc.jiandaoyun.com/open/11500

## 1. 简介

### 1.1 功能简介

俗称钩子，在简道云中是可以由开发人员自定义的回调地址。

这是用户通过自定义回调函数的方式来改变 Web 应用的一种行为，这些回调函数可以由不是该 Web 应用官方的第三方用户或者开发人员来维护，修改。通过 Webhook，你可以自定义一些行为通知到指定的 URL 去。Webhook 的“自定义回调函数”通常是由一些事件触发的。用户通过配置，就可以使一个网站上的事件调用在另一个网站上表现出来，这些事件调用可以是任何事件，但通常应用的是系统集成和消息通知。

![](https://help-assets.jiandaoyun.com/upload/nUYqx8nwtPRaEE-Vww-q1tFl.png)

### 1.2 使用场景

在产品管理系统中，当简道云有数据被删除或者修改时，可以通过 Webhook 将信息推送到第三方系统中。

### 1.3 版本说明

本功能为付费高级功能，需简道云企业版及以上版本可用。详情参见：[官网定价](https://www.jiandaoyun.com/index/price/)。

## 2. 设置步骤

### 2.1 设置入口

选择要设置 Webhook 的表单，点击「编辑表单>>扩展功能>>数据推送」，即可新建数据推送。

![](https://help-assets.jiandaoyun.com/595ff206-58ff-4ee7-99f3-7b4694b30392)

### 2.2 使用Webhook

Webhook 包含以下内容：

* [开发指南](https://hc.jiandaoyun.com/open/11507)
* [数据推送](https://hc.jiandaoyun.com/open/10732)
* [表单推送](https://hc.jiandaoyun.com/open/11501)
* [消息推送](https://hc.jiandaoyun.com/open/11497)

您可以通过阅读以上几篇文档内容，了解和学习如何使用简道云的 Webhook 功能。

## 3. 申请试用

标准版不包含 API 及 Webhook 功能，企业版及以上的用户可直接体验该功能，无需额外开通。

* [点击申请试用 - API & Webhook](https://jiandaoyun.com/f/5b72286213ab1f08a834ef08?ext=%E6%96%87%E6%A1%A311500)（价格咨询 / 功能测试 / 售前支持）
* [点击在线咨询](https://www.jiandaoyun.com/help/chat_online?source=business)

![](https://help-assets.jiandaoyun.com/upload/CUglZnElvLvQ)

注：使用 API 修改、新建、删除的数据，不会触发 Webhook 数据推送。

## 4. 代码示例

简道云 Webhook server 多语言 [调用示例](https://github.com/jiandaoyun/webhook-demo):

* [c#](https://github.com/jiandaoyun/webhook-demo/tree/master/c%23)
* [go](https://github.com/jiandaoyun/webhook-demo/tree/master/go)
* [java](https://github.com/jiandaoyun/webhook-demo/tree/master/java)
* [node](https://github.com/jiandaoyun/webhook-demo/tree/master/node)
* [php](https://github.com/jiandaoyun/webhook-demo/tree/master/php)
* [python](https://github.com/jiandaoyun/webhook-demo/tree/master/python)
* [ruby](https://github.com/jiandaoyun/webhook-demo/tree/master/ruby)

**本章内容：**

1. [开发指南](/open/11507)
2. [数据推送](/open/10732)
3. [表单推送](/open/11501)
4. [消息推送](/open/11497)