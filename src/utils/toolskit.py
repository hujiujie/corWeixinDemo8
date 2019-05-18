# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 11:28
# @Author  : hjj
# @Site    : 工具集，通用的工具都放在这里，很多模块都可以调用
# @File    : toolskit.py
import random
import time


# 更新字典值方法  json_obj是一个字典
def update_json_value_by_key(json_obj, key, new_value):
    json_obj[key] = new_value
    return json_obj


# 动态更新参数，在原来参数值的基础上加时间戳
def append_time_stamp_string(old_value):
    return old_value + "_" + time.strftime("%Y%m%d%H%M%S")


# 随机生成手机号
def get_random_mobile():
    for k in range(10):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                   "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                   "166", "177", "186", "187", "188", "189", "199"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 随机生成邮箱
def get_random_string(length=5):
    low_case = [chr(i) for i in range(65, 91)]
    up_cases = [chr(i) for i in range(97, 123)]
    all_string = "".join(low_case) + "".join(up_cases) + "0123456789"
    return "".join(random.choice(all_string) for i in range(length))

