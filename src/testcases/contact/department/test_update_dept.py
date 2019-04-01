# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 22:53
# @Author  : hjj
# @Site    : 
# @File    : test_update_dept.py
import pytest
from apis.contact.department.depmanagment import DeptManagment


class TestUpdateDept:
    @pytest.mark.parametrize("id,name", [(2,"测试更新"),(3,"测试更新3"),(4,"测试更新4")])
    def test_updtat_dept(self,id,name):
        dept_managment = DeptManagment()
        dept_managment.update_dept(id,name)
        update_res = dept_managment.get_response()
        assert update_res.get('errmsg') == 'updated'

