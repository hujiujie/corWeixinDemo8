# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 23:38
# @Author  : hjj
# @Site    : 通信录-成员
# @File    : test_member.py
from apis.contact.member.member_managerment import MemberManagermentApi


class TestMember:
    def test_create_member(self):
        member_obj = MemberManagermentApi()
        member_obj.create_member()
        res = member_obj.get_response()
        assert res.get('errmsg') == 'created'
