#! /usr/bin/env python
#coding=utf-8

import requests
response = requests.get(
    'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwd6da61649bd66fea&corpsecret=C7uGOrNyxWWzwBsUyWEbLdbZBDrc71PNOhyQ_YYPhts',
    verify=False,

    headers={'cache-control': 'no-cache', 'Postman-Token': '5a673687-449e-4914-8550-6c51283b4d6c', 'User-Agent': 'PostmanRuntime/7.6.1', 'Accept': '*/*', 'Host': 'qyapi.weixin.qq.com', 'accept-encoding': 'gzip, deflate', 'Connection': 'close', 'Pragma': 'no-cache'},
)
print(response.json())
