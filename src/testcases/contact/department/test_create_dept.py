#! /usr/bin/env python
# coding=utf-8
import pytest
from apis.contact.department.depmanagment import DeptManagment

# 创建部门
class TestCreateDept:

    # 创建一级.二级部门
    @pytest.mark.parametrize("pre_name,child_name", [("新增部门0403", "新增部门0403-1"),("新增部门04032", "新增部门04032-1")])
    def test_create_new_dep(self, pre_name,child_name):
        dept_managment = DeptManagment()
        dept_managment.create_dept(pre_name)
        create_res1 = dept_managment.get_response()
        parentid = create_res1.get("id")
        dept_managment.create_child_dept(child_name, parentid)
        create_res2= dept_managment.get_response()
        assert create_res2.get('errmsg') == 'created'

