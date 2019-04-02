# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 22:55
# @Author  : hjj
# @Site    : 获取部门列表
# @File    : test_list_dept.py
from apis.contact.department.depmanagment import DeptManagment


class TestListDetp:
    # id 部门id。获取指定部门及其下的子部门。 如果不填，默认获取全量组织架构
    def test_list_dept(self):
        dept_managment = DeptManagment()
        res = dept_managment.list_dept(id="")
        print(res.json())
        assert res.json().get('errmsg') == 'ok'









