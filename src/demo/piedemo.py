#! /usr/bin/env python
#coding=utf-8


from pyecharts import Pie

pie = Pie("成功率统计")

attr = ['失败','中断','通过','跳过','未知']
value= [12,22,34,29,16]

pie.add("", attr, value, is_label_show=True)
#pie.render('../html/Pie1.html')
pie.render(path='th.jpeg')