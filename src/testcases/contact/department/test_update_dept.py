# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 22:53
# @Author  : hjj
# @Site    : 更新部门接口
# @File    : test_update_dept.py
import pytest
from apis.contact.department.depmanagment import DeptManagment


class TestUpdateDept:
    @pytest.mark.parametrize("id,name", [(2,"测试更新2"),(3,"测试更新3"),(4,"测试更新4"),(5,"测试更新5"),(6,"测试更新6"),(7,"测试更新7"),(8,"测试更新8"),(9,"测试更新9"),(10,"测试更新10"),(11,"测试更新11"),(12,"测试更新12"),(13,"测试更新13")])
    def test_updtat_dept(self,id,name):
        dept_managment = DeptManagment()
        dept_managment.update_dept(id,name)
        update_res = dept_managment.get_response()
        assert update_res.get('errmsg') == 'updated'

