# 流程推送

URL: https://hc.jiandaoyun.com/open/23345

## 1. 简介

### 1.1 功能简介

流程变更时推送，指的是当流程状态变更、流程待办变更以及产生抄送时，自动将流程推送到指定服务器，实现简道云与第三方系统的实时对接。

### 1.2 使用场景

适用于需要将简道云流程相关信息同步到第三方系统中处理的场景。

### 1.3 预期效果

以「流程状态变更时」推送为例，当管理员结束流程时，系统会自动将该变更推送至指定服务器。效果如下所示：

![](https://help-assets.jiandaoyun.com/efba1f72-dfa4-46c6-ae30-9b722e9f18ad?attname=image.png)

## 2. 设置步骤

### 2.1 设置入口

在「扩展功能 >> 数据推送」处，点击「新建数据推送」，即可创建一个数据推送事件。

![](https://help-assets.jiandaoyun.com/ed62276a-5605-49ee-8988-880225c281f8?attname=image.png)

### 2.2 设置服务器

#### 2.2.1 选择目标服务器

进入数据推送设置页面后，选择目标服务器为「自定义服务器」。

![](https://help-assets.jiandaoyun.com/6838510e-770d-4bd4-9e67-b434cefdfbd2?attname=image.png)

注：流程推送中，目标服务器仅支持选择「自定义服务器」。

#### 2.2.2 设置服务器地址

企业根据自身的企业需求，可填写指定的服务器地址。

![](https://help-assets.jiandaoyun.com/d2f6c5ae-1ba9-4376-8d19-195dbe9aaed7?attname=image.png)

#### 2.2.3 生成Secret

服务器地址填写完成后，点击「生成 Secret」，系统将自动生成对应的 Secret。

![](https://help-assets.jiandaoyun.com/4475c78a-a05a-4ae6-9596-51e207e96e57?attname=image.png)

#### 2.2.4 服务器连接测试

服务器地址确认无误及生成 Secret 后，点击「服务器连接测试」，系统将自动进行服务器连接测试，测试成功后，则显示「服务器连接成功」。

![](https://help-assets.jiandaoyun.com/746446be-e40b-4986-9c86-30b2117b4b4f?attname=image.png)

### 2.3 设置推送类型和事件

进行流程推送设置时，推送类型和推送事件选择如下所示：

* 推送类型：选择「流程变更时推送」；
* 推送事件：企业可根据自身需求进行勾选，不同事件含义如下：

+ 流程状态变更时：在流程状态变化时推送；
+ 流程待办变更时：在待办产生、被处理（如提交、加签、回退等）时推送；
+ 产生抄送时：有抄送产生时推送。

全部设置完成后，点击「保存」。

![](https://help-assets.jiandaoyun.com/d93180f1-a55e-4685-ab6b-59335440ca5a?attname=image.png)

### 2.4 查看推送日志

数据推送完成后，点击数据推送事件右侧的「推送日志」，即可查看推送详情。支持查看以下数据推送详情：

* 推送失败日志
* 推送成功日志
* 全部日志

![](https://help-assets.jiandaoyun.com/e1d23aa8-0dbc-463c-9ee7-9c5f4e9c8fe5?attname=image.png)

注：流程推送失败后，不支持手动重新推送，系统将间隔 5min、15min、1h 和 2h 自动重试。

### 2.5 效果演示

效果参见本文【1.3 预期效果】。

## 3. 注意事项

简道云提供 3 种流程数据与外部系统互通的方式，以满足不同场景下的业务需求。详情可查看：[流程数据对接第三方系统指南](https://hc.jiandaoyun.com/doc/23343)。