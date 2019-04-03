# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 23:38
# @Author  : hjj
# @Site    : 通信录-成员
# @File    : test_member.py
import pytest

from apis.contact.member.member_managerment import MemberManagermentApi


class TestMember:


    # 创建成员,读取一个json文件
    def test_create_member(self):
        self.member_obj = MemberManagermentApi()
        self.member_obj.create_member("../testdata/member.json")
        res = self.member_obj.get_response()
        assert res.get('errmsg') == 'created'

    # 创建成员,读取多个json文件
    # 需要安装pytest-datafiles依赖
    @pytest.mark.datafiles(
        '../testdata/member1.json',
        '../testdata/member2.json',
        '../testdata/member3.json')
    def test_create_new_member(self, datafiles):
        for member_file in datafiles.listdir():
            self.member_obj = MemberManagermentApi()
            self.member_obj.create_member(member_file)
            create_res = self.member_obj.get_response()
            assert create_res.get('errmsg') == 'created'

    # 读取成员列表
    def test_get_member_list(self):
        member_obj = MemberManagermentApi()
        res = member_obj.get_member_list(userid="zhangsan")
        print(res.json())
        assert res.json().get("errmsg") == "ok"