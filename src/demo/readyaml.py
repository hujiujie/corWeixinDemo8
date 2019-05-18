#! /usr/bin/env python
#coding=utf-8
import codecs
import yaml

with codecs.open("my.yaml",'r',encoding='utf-8') as load_f:
    load_dict = yaml.load(load_f)
    print(load_dict.get('spouse').get('name'))

with codecs.open("m1.yaml","w",encoding='utf-8') as dump_f:
    load_dict["broker"] = 0
    yaml.dump(load_dict,dump_f,allow_unicode=True,default_flow_style=False)