#! /usr/bin/env python
#coding=utf-8

import emails
import codecs


#message = emails.Message(html="<img src='th.jpeg'>",mail_from=('测试部', '361631212@qq.com'))
message = emails.Message(html=codecs.open('mailcontent.html',encoding='utf8'),
                         subject='测试报告',
                         mail_from=('测试部', 'xxxxx@qq.com'))

message.attach(filename='th.jpeg', data=open('th.jpeg', 'rb'))
message.attachments['th.jpeg'].is_inline = True
message.transformer.synchronize_inline_images()
message.transformer.save()
message.html
u'<html><body><img src="cid:th.jpeg"></body></html>'
message.send(to=('22', 'rrrrr@163.com'),
             smtp={'host':'smtp.qq.com', 'port': 465, 'ssl': True, 'user': 'xxxxxxxxx@qq.com', 'password': '123456'})
