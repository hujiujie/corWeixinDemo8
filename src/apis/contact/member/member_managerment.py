# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 23:26
# @Author  : hjj
# @Site    :  通讯录管理--成员管理
# @File    : member_managerment.py
import logging

from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_cfg


class MemberManagermentApi(BaseAPI):
    def __int__(self):
        BaseAPI.__init__()
        logging.info("Init member API")
        self.dep_secure = sys_cfg.get('contact_para', 'secure')
        self.create_member_url = sys_cfg.get('contact_para', 'create_member_url')
        self.get_member_url = sys_cfg.get('contact_para', 'get_member_url')
        self.update_member_url = sys_cfg.get('contact_para', 'update_member_url')
        self.delete_member_url = sys_cfg.get('contact_para', 'delete_member_url')

    # 创建成员
    def create_member(self):
        new_member = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "15913215421",
            "department": [1, 2],
            "order": [10, 40],
            "position": "产品经理",
            "gender": "1",
            "email": "zhangsan@gzdev.com",
            "is_leader_in_dept": [1, 0],
            "enable": 1,
            "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
            "telephone": "020-123456",
            "address": "广州市海珠区新港中路",
        }
        param = {"access_token": self.get_token(self.dep_secure)}
        self.post_json(self.create_member_url,json_obj=new_member,params=param)