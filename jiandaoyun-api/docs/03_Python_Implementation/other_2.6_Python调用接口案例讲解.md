# 2.6 Python调用接口案例讲解

URL: https://hc.jiandaoyun.com/open/12054

![](https://help-assets.jiandaoyun.com/upload/h2DN2XcfoG0l)

**本节主题：**2.6 Python调用接口案例讲解

**课程讲师：**Yunlin

**观看地址：**[点我进入](https://edu.fanruan.com/video/181)

## 1 本节要点

* 上期作业讲解
* 了解POSTMAN CODE功能
* Python调用接口演示

## 2 课前准备

无

## 3 课程内容

### 3.1 上期作业讲解

（演示）

### 3.2 POSTMAN CODE

（演示 - 使用POSTMAN快速生成接口调用代码）

![](https://help-assets.jiandaoyun.com/upload/Bw6uuEomEV0n)

### 3.3 简道云的demo演示

（演示 - 使用Requests及Json库定义函数调用简道云的API接口

* 复制POSTMAN的CODE至Python，注意Body要替换成POSTMAN Body里面的内容（POSTMAN CODE里面的body内容有一些乱，使用原始的Json更好）

![](https://help-assets.jiandaoyun.com/upload/g6Ib557NiRlR)

```
import requests

url = "https://api.jiandaoyun.com/api/v1/app/5dce13f43087860006c70e7a/entry/5dce145c26aecf00062e7db0/data_retrieve"

#替换Body前
payload = "{\r\n    \"data_id\": \"5dd6740646357c0006e6eb6e\"\r\n}"
#替换Body后
payload = {
          "data_id": "5dd6740646357c0006e6eb6e"
      }

headers = {
  'Authorization': 'Bearer xxxxxxx',
  'Content-Type': 'application/json',
  'Cookie': 'JDY_SID=s%3AkkffLPwwM05AA85K8IdYsXPF0zB-I0fi.GLHEBt5s61l9x0S7idpqYTFPIoUccDRv4IdXRYertCU; DEV_SID=s%3AdpxME_zPEoygRg8TxawKi6TQsalZ8p-V.mYUJRUHwMd95JFvz1tg2Zssl%2B4a%2BQRVq%2FGSckENfixY'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```

* 定义函数，替换payload的参数为函数的变量，注意要把payload转换成Json![](https://help-assets.jiandaoyun.com/upload/ZnQVvCdKxF1T)

```
import requests
import json

def jdy(dataid):
    url = "https://api.jiandaoyun.com/api/v1/app/5dce13f43087860006c70e7a/entry/5dce145c26aecf00062e7db0/data_retrieve"

    payload = {
        "data_id": dataid
    }
    headers = {
      'Authorization': 'Bearer xxxxxxxxx',
      'Content-Type': 'application/json',
      'Cookie': 'JDY_SID=s%3AkkffLPwwM05AA85K8IdYsXPF0zB-I0fi.GLHEBt5s61l9x0S7idpqYTFPIoUccDRv4IdXRYertCU; DEV_SID=s%3AdpxME_zPEoygRg8TxawKi6TQsalZ8p-V.mYUJRUHwMd95JFvz1tg2Zssl%2B4a%2BQRVq%2FGSckENfixY'
    }

#注意，这里要把payload转换成Json
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

#最后只要打印出response.text即可，requests会自动把字节编码成字符串！
    print(response.text)
```

* 下面即可开始调用你的函数了！！！

```
jdy("5dd6740646357c0006e6eb6e")
```