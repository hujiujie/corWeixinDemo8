#! /usr/bin/env python
# coding=utf-8
import logging
from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_cfg


class DeptManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department management API")
        self.create_dep_url = sys_cfg.get('contact_para', 'create_dept_url')
        self.update_dep_url = sys_cfg.get('contact_para', 'update_dept_url')
        self.dep_secure = sys_cfg.get('contact_para', 'secure')

    # 创建部门
    def create_dept(self,name):
        new_part = {
            "name": name,
            "parentid": 1,
            "order": 1
        }

        param = {'access_token': self.get_token(self.dep_secure)}
        logging.debug("url:" + str(self.create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_dep_url, new_part, params=param)

    def get_create_dept_res(self):
        return self.get_response()

    # 更新部门
    def update_dept(self,id,name):
        update_part = {"id": id,"name":name}
        param = {"access_token":self.get_token(self.dep_secure)}
        self.post_json(self.update_dep_url,update_part,params=param)

    def get_update_dept_res(self):
        return self.get_response()
