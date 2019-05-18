#! /usr/bin/env python
#coding=utf-8

import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://xueqiu.com/',
    'Origin': 'https://xueqiu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

params = (
    ('symbol', 'SH000001,SZ399001,SZ399006,HKHSI,HKHSCEI,HKHSCCI,.DJI,.IXIC,.INX'),
)

response = requests.get('https://stock.xueqiu.com/v5/stock/batch/quote.json', headers=headers, params=params,verify=False)

print(response.json())