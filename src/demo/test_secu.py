#! /usr/bin/env python
#coding=utf-8

import base64
import requests

def test_security():
    response =requests.get('http://127.0.0.1:5000/hello')
    print(response.json())
    assert base64.b64decode(response.json().get('hello')).decode("utf-8")=='world'
