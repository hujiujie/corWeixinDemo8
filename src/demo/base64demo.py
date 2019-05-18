#! /usr/bin/env python
#coding=utf-8
import base64

code = base64.b64encode(b'world').decode("utf-8")

print(base64.b64decode(code).decode("utf-8"))