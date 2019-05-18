# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 13:02
# @Author  : hjj
# @Site    : 
# @File    : test_create_member4.py
from apis.contact.member.member_managerment import MemberManagermentApi
from utils import toolskit, comparator


class TestCreateMember4:
    # 动态更新用户名 手机号 邮箱
    # 通过配置文件，发送req请求，并通过配置文件比较返回结果（全量比较）
    # 如果开发修改了返回信息 ，那么只需要修改配置文件就行，不用修改很多地方的断言
    def test_create_new_member4(self):

        member_managment = MemberManagermentApi()
        json_obj=member_managment.get_json_obj_from_file_with_reqres('../testdata/member4.json',"testcase2","req")

        # 定义新用户名加时间戳的方法 这样每次保证用户名不一样
        new_userid = toolskit.append_time_stamp_string(json_obj.get("userid"))
        new_mobile = toolskit.get_random_mobile()

        # 获取随机生成的邮箱前缀
        email_prefix = toolskit.get_random_string()
        # 邮箱后缀json文件中email格式的固定后缀 一般企业微信邮箱后缀是固定的
        email_postfix =json_obj.get("email").split("@")[1]
        new_email= email_prefix + "@" + email_postfix

        # 字典值用户名对应更新
        toolskit.update_json_value_by_key(json_obj,"userid",new_userid)
        toolskit.update_json_value_by_key(json_obj, "mobile", new_mobile)
        toolskit.update_json_value_by_key(json_obj, "email", new_email)

        member_managment.create_member_by_json_obj(json_obj)

        # 当前返回的json串  与 预先定义好的member.json数据中res中的数据值 做比较
        live_create_res = member_managment.get_response()
        std_json_obj_res = member_managment.get_json_obj_from_file_with_reqres('../testdata/member4.json', "testcase2",
                                                                          "res")
        json_comparator = comparator.JsonComparator()

        # 断言两个json中的res中的值是否相等
        assert json_comparator.equal(live_create_res,std_json_obj_res)

        #扩展  如果是时间值比较 可以用大于 或小于某个时间
