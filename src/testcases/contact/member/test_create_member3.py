# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 13:02
# @Author  : hjj
# @Site    : 
# @File    : test_create_member3.py
from apis.contact.member.member_managerment import MemberManagermentApi


class TestCreateMember3:
    # 创建成员，读取json文件，一个json文件中存在多个成员信息
    def test_create_member3(self):
        member_obj = MemberManagermentApi()
        json_obj = member_obj.get_json_obj_from_file('../testdata/member3.json', "testcase1")
        member_obj.create_member_by_json_obj(json_obj)
        create_res = member_obj.get_response()
        assert create_res.get('errmsg') == 'created'
