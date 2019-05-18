#! /usr/bin/env python
#coding=utf-8

import requests
import base64

def test_base64api():
    res= requests.get("http://127.0.0.1:5000/hello")
    #print(res.json())
    #print(base64.b16decode(res.json().get('hello')))
    assert base64.b64decode(res.json().get('hello')).decode("utf-8") =='world'