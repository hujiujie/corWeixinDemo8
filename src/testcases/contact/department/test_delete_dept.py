# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 21:53
# @Author  : hjj
# @Site    : 删除部门
# @File    : test_delete_dept.py
import pytest

from apis.contact.department.depmanagment import DeptManagment


class TestDeleteDept:
    @pytest.mark.parametrize("id",[10])
    def test_delete_dept(self,id):
        dept_managment = DeptManagment()
        res = dept_managment.delete_dept(id)
        assert res.json().get('errmsg') == 'deleted'

