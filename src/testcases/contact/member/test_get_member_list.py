# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 13:03
# @Author  : hjj
# @Site    : 
# @File    : test_get_member_list.py
from apis.contact.member.member_managerment import MemberManagermentApi


class TestMemberList:

    # 读取成员列表
    def test_get_member_list(self):
        member_obj = MemberManagermentApi()
        res = member_obj.get_member_list(userid="zhangsan")
        print(res.json())
        assert res.json().get("errmsg") == "ok"
