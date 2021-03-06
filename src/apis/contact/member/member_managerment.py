# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 23:26
# @Author  : hjj
# @Site    :  通讯录管理--成员管理
# @File    : member_managerment.py
import codecs
import json
import logging

import requests

from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_cfg


class MemberManagermentApi(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init member API")
        self.create_member_url = sys_cfg.get('contact_para', 'create_member_url')
        self.get_member_url = sys_cfg.get('contact_para', 'get_member_url')
        self.update_member_url = sys_cfg.get('contact_para', 'update_member_url')
        self.delete_member_url = sys_cfg.get('contact_para', 'delete_member_url')
        self.dep_secure = sys_cfg.get('contact_para', 'secure')

    # 读取json文件，文件中只有一个成员信息 ，对应member1.json格式
    def get_new_member(self,file_name):
        with codecs.open(file_name,'r',encoding='utf8') as f:
            json_object = json.loads(f.read(),encoding='utf8')
            logging.debug('json_object'+str(json_object))
            return json_object


    # 读取json文件，json文件中有多个成员信息，对应member3.json格式
    def get_json_obj_from_file(self,file_name,testcase_name):
        with codecs.open(file_name,'r',encoding='utf8') as f:
            multiple_json_object = json.loads(f.read(),encoding='utf8')
            case_json_object=multiple_json_object.get(testcase_name)
            logging.debug('json_object'+str(case_json_object))
            return case_json_object


    # 动态更新参数，对应member4.json格式
    def get_json_obj_from_file_with_reqres(self,file_name,testcase_name,type):
        with codecs.open(file_name,'r',encoding='utf8') as f:
            multiple_json_object = json.loads(f.read(),encoding='utf8')
            case_json_object=multiple_json_object.get(testcase_name).get(type)
            logging.debug('json_object'+str(case_json_object))
            return case_json_object



    # 创建成员 json文件中有多个成员信息，对应member3.json格式
    def create_member_by_json_obj(self,json_object):
        param = {'access_token':self.get_token(self.dep_secure)}
        logging.debug("params:" + str(param))
        self.post_json(self.create_member_url,json_object,params=param)

    # 创建成员 json文件中只有一个成员信息 ，对应member1.json格式
    def create_member(self,file_name):
        new_member = self.get_new_member(file_name)
        param = {"access_token": self.get_token(self.dep_secure)}
        logging.debug("url=" + str(self.create_member_url))
        logging.debug("param=" + str(param))
        self.post_json(self.create_member_url,json_obj=new_member,params=param)

    # 读取成员列表
    def get_member_list(self,userid):
        param = {"access_token": self.get_token(self.dep_secure),"userid" : userid}
        return requests.get(self.get_member_url, params=param)