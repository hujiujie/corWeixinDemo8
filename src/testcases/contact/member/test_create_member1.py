# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 23:38
# @Author  : hjj
# @Site    : 通信录-成员
# @File    : test_member.py

from apis.contact.member.member_managerment import MemberManagermentApi


class TestCreateMember:

    # 创建成员,读取一个json文件，一个json文件中一个成员信息
    def test_create_member(self):
        member_obj = MemberManagermentApi()
        member_obj.create_member("../testdata/member.json")
        res = member_obj.get_response()
        assert res.get('errmsg') == 'created'
