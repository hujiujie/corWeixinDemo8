#! /usr/bin/env python
#coding=utf-8

from pyecharts import Pie

pie =Pie('测试用例成功率统计',background_color = 'white')
attr = ['失败','中断','通过','跳过','未知']
value= [12,22,34,29,16]
pie.add('',attr,value,radius=[65, 75],center=[50, 50],is_label_show=True)
#pie.add('',attr,v1,radius=[0, 60],center=[50, 50],rosetype='area')
pie.render(path = 'cycle.jpeg')
