# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 13:04
# @Author  : hjj
# @Site    : 
# @File    : test_create_member2.py
import pytest

from apis.contact.member.member_managerment import MemberManagermentApi


class TestCreateMember2:
    # 创建成员,读取多个json文件，一个json文件中一个成员信息
    # 需要安装pytest-datafiles依赖
    @pytest.mark.datafiles(
        '../testdata/member1.json',
        '../testdata/member2.json'
    )
    def test_create_member2(self, datafiles):
        for member_file in datafiles.listdir():
            member_obj = MemberManagermentApi()
            member_obj.create_member(member_file)
            create_res = member_obj.get_response()
            assert create_res.get('errmsg') == 'created'
