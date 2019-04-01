#! /usr/bin/env python
# coding=utf-8
import pytest
from apis.contact.department.depmanagment import DeptManagment


class TestCreateDept:

    @pytest.mark.parametrize("name", ["研发部-2", "产品部-2", "运营部-2", "市场部-2", "财务部-2"])
    def test_create_new_dep(self, name):
        dept_managment = DeptManagment()
        dept_managment.create_dept(name)
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg') == 'created'
