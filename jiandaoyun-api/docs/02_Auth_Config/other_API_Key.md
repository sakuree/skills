# API Key

URL: https://hc.jiandaoyun.com/open/16782

## 1. 简介

### 1.1 功能简介

API Key，即 API 密钥，是赋予某种形式的秘密令牌的名称，与 Web 服务（或类似的）请求一起提交以识别请求的来源。密钥可以包含在请求内容的某个摘要中，以进一步验证来源并防止篡改这些值。

### 1.2 使用场景

如在配置前端事件调用部分插件时，需要开启 API 功能后，才能成功配置使用插件。

### 1.3 预期效果

以天聚数行插件配置中，需要配置简道云 API 后才能开启插件为例。如下所示：

![](https://help-assets.jiandaoyun.com/5c1fe48f-b06c-49e8-ae36-5b0a64ba1c26?attname=image.png)

## 2. 设置步骤

### 2.1 设置入口

在「开放平台 >> 密钥管理」处，选择「API Key」，即可对 API Key 进行创建、设置等操作。

![](https://help-assets.jiandaoyun.com/c182bab7-6bc1-4dfd-944b-12830e775dfd?attname=image.png)

### 2.2 创建API

1）点击「创建API Key」，在API 列表中系统会自动创建出成一条 API Key。如下所示：

![](https://help-assets.jiandaoyun.com/512dc732-9f85-4d80-a08c-2a4490864fb9?attname=image.png)

注：

1）一个账户最多创建 500 个 API Key。

2）系统自动生成的 API Key 数据不可修改。

2）API Key 默认隐藏不显示，点击旁边的小眼睛图标即可显示 API Key 全部内容。

![](https://help-assets.jiandaoyun.com/5ea5ff17-63ad-475b-99fc-b5bd6e98df78?attname=image.png)

### 2.3 修改API名称

API Key 生成后，点击生成的 API Key所在行，进入 API Key 信息详情页面，在「名称」处，可以修改 API 名称，以便区分多个 API。

![](https://help-assets.jiandaoyun.com/0e3735d0-5a55-45c2-8faf-5f63ede88a70?attname=image.png)

### 2.4 授权范围

点击 API Key 所在行，进入 API Key 信息详情页面，可对「应用授权范围」和「接口授权范围」进行设置。如下所示：

![](https://help-assets.jiandaoyun.com/22bcb291-b897-40b9-a5d2-c18de181a818?attname=image.png)

#### 2.4.1 应用授权范围

应用授权范围支持「全部应用」和「部分应用」两种范围：

* 若选择「全部应用」，则简道云工作台中所有应用都可使用该API Key；
* 若选择「部分应用」，则仅添加进应用列表中的应用可以使用该 API Key。

![](https://help-assets.jiandaoyun.com/a35a4f3b-a3e4-4828-9904-ea610e780786?attname=image.png)

#### 2.4.2 接口授权范围

接口授权范围支持「全部接口」和「部分接口」两种范围：

* 若选择「全部接口」，则简道云中所有接口都可使用该API Key。包括通讯录接口、应用接口、表单接口、数据接口、文件接口、流程接口和 CRM 接口。
* 若选择「部分接口」，则仅添加进接口列表中的接口可以使用该 API Key。

![](https://help-assets.jiandaoyun.com/2a2d7167-a703-4172-936f-da0f863dad98?attname=image.png)

### 2.5 IP 白名单

设置 IP 白名单后，只有来自白名单范围内的IP地址的请求才会被正常处理，不在白名单内的 IP 地址的请求不会成功。

点击 API Key 所在行，进入 API Key 信息详情页面，在「IP 白名单」处，点击「添加 IP」。如下所示：

![](https://help-assets.jiandaoyun.com/e7ad95dd-cc79-4a25-96ce-d2fc73bedf8b?attname=image.png)

在 IP 白名单内，支持设置单个 IP 地址或 IP 地址段。设置 IP 地址段时仅支持带一个 **\* 号**通配符的 IP 格式。如下所示：

![](https://help-assets.jiandaoyun.com/7e9ad1f5-2cad-4839-8e35-ce6e84b90363?attname=image.png)

注：

1）若未设置任何白名单，则任何 IP 均可使用对应的 API Key。

2）若未设置任何白名单的情况下，所有插件都可调用该 API Key；若已设置了白名单时，所有插件都不可调用该 API Key。

3）不对企业内所有 IP 总数量设置上限，而是对每个 API Key 内的白名单IP数量设置上限。每个 API Key 内的白名单 IP 数量上限为 50 个。

4）IP 白名单内，暂不支持 IPV6 地址。

### 2.6 停用/启用

在「状态」处，通过关闭/开启状态开关，对于已经创建的密钥可以进行停用，停用的密钥也可以重新开启使用。

![](https://help-assets.jiandaoyun.com/b1bd8853-ad5c-4f75-9a39-b57d5dcff1e2?attname=image.png)

### 2.7 复制

#### 2.7.1 复制密钥值

在 API Key 的密钥值处，点击复制图标，即可快捷复制密钥值后并进行应用。如下所示：

![](https://help-assets.jiandaoyun.com/03f08b94-b3d5-4589-bced-bf547cbde0df?attname=image.png)

#### 2.7.2 复制整条API Key

在 API Key 的操作处，点击复制图标，即可复制整条 API Key。复制后，API Key 的授权范围和 IP 白名单会同步复制，但复制后的 API Key 会生成新的密钥值。如下所示：

![](https://help-assets.jiandaoyun.com/8f02d371-d493-483d-b9c6-dbb00abe7d4b?attname=image.png)

### 2.8 删除

对于不需要使用的 API Key 可以进行删除。由于API Key 的重要性，也可以通过删除再新建的方式进行 API Key 的定期更换。

![](https://help-assets.jiandaoyun.com/85625834-c243-4b47-9aa2-f7a9bfcb4510?attname=image.png)

注：删除前请确认该 API Key 没有被使用。