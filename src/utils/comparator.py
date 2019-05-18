# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 13:05
# @Author  : hjj
# @Site    : 对断言结果参数和参数值做比较
# @File    : comparator.py
import logging

class JsonComparator:

    def __init__(self):
        pass

    def equal(self,live_json,std_json):
        logging.info('live_json:'+str(live_json))
        logging.info('std_json:' + str(std_json))
        return live_json==std_json

    def less_than(self,live_json,std_json):
        '''
        compare two json object, if std_json contains live_json
        (live_json<=std_json)
        return True, else return false
        :param live_json:
        :param std_json:
        :return:
        '''
        pass

    def more_than(self,live_json,std_json):
        '''
        compare two json object, if live_json contains std_json
        (live_json>=std_json)
        return True, else return false
        :param live_json:
        :param std_json:
        :return:
        '''
        pass


if __name__=='__main__':
    json_comparatorr= JsonComparator()
    live_json={
      "errcode": 0,
      "errmsg": "created"
    }
    std_json = {
        "errcode": 0,
        "errmsg": "created"
    }
    print(json_comparatorr.equal(live_json,std_json))