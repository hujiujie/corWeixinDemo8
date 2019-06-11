# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 13:30
# @Author  : hjj
# @Site    : 类名与测试用例json文件名一致； 方法名与测试用例case名相似，可以通过方法名取到用例名称
# @File    : test_create_member6.py
import sys

import allure

from apis.contact.member.member_managerment import MemberManagermentApi
from utils import toolskit, comparator

@allure.feature("创建用户")

class TestCreateMember123:
    # 此测试用例，测试数据通过类名和方法名获得
    # 但是必须确保类名和json文件名称一致
    @allure.story("创建用户test1")
    def test_testcase1(self):

        # 如果类中只有一个方法，则可以用类名，获取类名
        class_name = self.__class__.__name__

        # 获取用例名  json数据中的参数必须设置为testcase1 与这里的方法名保持一致，才好获取
        case_name = sys._getframe().f_code.co_name.split("_")[1]

        member_managment = MemberManagermentApi()
        json_obj=member_managment.get_json_obj_from_file_with_reqres('../testdata/'+ class_name +'.json',case_name,"req")

        new_userid = toolskit.append_time_stamp_string(json_obj.get("userid"))
        new_mobile = toolskit.get_random_mobile()
        email_prefix = toolskit.get_random_string()
        email_postfix =json_obj.get("email").split("@")[1]
        new_email= email_prefix + "@" + email_postfix

        toolskit.update_json_value_by_key(json_obj,"userid",new_userid)
        toolskit.update_json_value_by_key(json_obj, "mobile", new_mobile)
        toolskit.update_json_value_by_key(json_obj, "email", new_email)

        member_managment.create_member_by_json_obj(json_obj)

        live_create_res = member_managment.get_response()
        std_json_obj_res = member_managment.get_json_obj_from_file_with_reqres('../testdata/' + class_name + '.json',
                                                                               case_name,
                                                                               "res")
        json_comparator = comparator.JsonComparator()

        # 断言两个json中的res中的值是否相等
        assert json_comparator.equal(live_create_res, std_json_obj_res)

    @allure.story("创建用户test2")
    def test_testcase2(self):

        # 如果类中只有一个方法，则可以用类名，获取类名
        class_name = self.__class__.__name__

        case_name = sys._getframe().f_code.co_name.split("_")[1]

        member_managment = MemberManagermentApi()
        json_obj=member_managment.get_json_obj_from_file_with_reqres('../testdata/'+ class_name +'.json',case_name,"req")

        new_userid = toolskit.append_time_stamp_string(json_obj.get("userid"))
        new_mobile = toolskit.get_random_mobile()
        email_prefix = toolskit.get_random_string()
        email_postfix =json_obj.get("email").split("@")[1]
        new_email= email_prefix + "@" + email_postfix

        toolskit.update_json_value_by_key(json_obj,"userid",new_userid)
        toolskit.update_json_value_by_key(json_obj, "mobile", new_mobile)
        toolskit.update_json_value_by_key(json_obj, "email", new_email)

        member_managment.create_member_by_json_obj(json_obj)

        live_create_res = member_managment.get_response()
        std_json_obj_res = member_managment.get_json_obj_from_file_with_reqres('../testdata/'+ class_name +'.json', case_name,
                                                                          "res")
        json_comparator = comparator.JsonComparator()

        # 断言两个json中的res中的值是否相等
        assert json_comparator.equal(live_create_res,std_json_obj_res)