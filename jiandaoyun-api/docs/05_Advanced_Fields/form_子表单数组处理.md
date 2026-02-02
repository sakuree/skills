# 子表单数组处理

URL: https://hc.jiandaoyun.com/open/12208

前端事件对于子表字段的支持可以分为两种情况：

1. 触发字段为主表字段，返回字段为子表字段
2. 触发字段为子表字段，返回字段也为子表字段

## 4.1 触发字段为主表字段

触发字段为主表字段，返回值字段为子表字段时，可以接收数组数据，并且自动按数组的行数创建相同行数的子表单。如下图中，可以自动将快递的时间、状态信息（数组）写入子表单中，根据数组的行数自动创建子表单行。

![](https://help-assets.jiandaoyun.com/upload/p4TXO6y0HxnU)

Jsonpath配置方式：使用[\*]可以选取不固定长度的数组，数组里面每有一行会自动在子表单创建一行；

例如返回数据为：

```
{
    "showapi_res_body": {
        "data": [
            {
                "context": "【江苏省无锡市安镇二部公司】 已收入",
                "time": "2020-08-19 07:52:41"
            },
            {
                "context": "【江苏省无锡市锡新开发区】 已发出 下一站 【江苏省无锡市安镇镇一部公司】",
                "time": "2020-08-19 06:40:22"
            },
            {
                "context": "【江苏省无锡市锡新开发区公司】 已收入",
                "time": "2020-08-19 06:20:16"
            },
            {
                "context": "【无锡转运中心】 已发出 下一站 【江苏省无锡市锡新开发区公司】",
                "time": "2020-08-19 04:16:37"
            }
        ]
    }
}
```

原先我们获取数组一行的时间的话，需要使用：

```
$['showapi_res_body']['data'][0]['time']
```

这里的[0]表示索引数组第一行的数据。而如果我们是要获取数组里面所有的time，根据其行数自动在子表单创建行，则可以写成:

```
$['showapi_res_body']['data'][*]['time']
```

## 4.2 触发字段为子表字段

触发字段为子表字段，返回值字段也为子表字段时，与触发字段和返回值字段都是主表字段的情况类似，触发字段和返回值字段在子表单的同一行内存在对应关系。

以下图中的天气查询为例，城市字段为触发字段，当输入省份和城市之后，将会自动触发前端事件查询天气并返回天气值写入子表单同一行中对应的天气字段内。

![](https://help-assets.jiandaoyun.com/upload/g7dNJELXBlvG)

此时返回数据为：

```
{
    "ret": 200,
    "data": {
        "cityinfo": {
            "provinces": "江苏",
            "city": "无锡",
            "area": "无锡",
            "id": "101190201",
            "prov_py": "jiangsu",
            "city_py": "wuxi",
            "qh": "0510",
            "jb": "2",
            "yb": "214000",
            "area_py": "wuxi",
            "area_short_code": "wx",
            "lng": "120.301663",
            "lat": "31.574729"
        },
        "now": {
            "id": "101190201",
            "area_name": "无锡",
            "city": {
                "night_air_temperature": "7",
                "day_air_temperature": "13",
                "wind_direction": "东北风转北风",
                "wind_power": "<3级",
                "weather": "多云",
                "weather_code": "01"
            },
            "detail": {
                "time": "15:30",
                "date": "12月01日",
                "week": "二",
                "temperature": "12",
                "wind_direction": "东北风",
                "wind_direction_str": "NE",
                "wind_power": "2级",
                "wind_speed": "<12km/h",
                "humidity": "58%",
                "weather": "多云",
                "weather_code": "01",
                "weather_english": "Cloudy",
                "qy": "1027",
                "njd": "14.6km",
                "rain": "0",
                "aqi": "39",
                "quality": "优",
                "aqi_pm25": "57",
                "nongli": "十月十七",
                "sun_begin": "06:40",
                "sun_end": "16:55",
                "so2": "68",
                "o3": "34",
                "co": "26",
                "no2": "9",
                "pm10": "1",
                "kinect": "11",
                "shadow_kinect": "10.0",
                "ultraviolet_rays": "2级",
                "ultraviolet_rays_status": "低",
                "pressure_change": "稳定",
                "cloud_amount": "91%"
            },
            "update_time": 1606809680,
            "alarm_list": []
        }
    },
    "qt": 0.009
}
```

那么，只需要将子字段“天气”的返回值设置为：

```
$['data']['now']['detail']['weather']
```