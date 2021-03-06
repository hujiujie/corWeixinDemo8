#! /usr/bin/env python
#coding=utf-8
import subprocess
import sys
import logging
import os
import pytest

#Add src root dirctory to PYTHONPATH by extend sys.path
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
from initialization import sysconfig

fileHandler = logging.FileHandler(filename="../log/auto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)


if __name__ == '__main__':
    logging.info("Start to execute  automation cases")

    pytest.main(['-s', '-q', '-v', '--alluredir', 'result','testcases/'])
    #pytest.main(['-sq', 'testcases/'])
    #pytest.main(['-sq', 'testcases/contact/department/test_create_dept.py'])
    #pytest.main(['-sq', 'testcases/contact/department/test_update_dept.py'])
    #pytest.main(['-sq', 'testcases/contact/department/test_delete_dept.py'])
    #pytest.main(['-sq', 'testcases/contact/department/test_list_dept.py'])
    #pytest.main(['-sq', 'testcases/contact/member/test_create_member7.py'])
    #pytest.main(['-sq','--alluredir', '../log/testreport', 'testcases/contact/member/test_create_member7.py'])
    #print(subprocess.getstatusoutput('allure generate --clean ../log/testreport/ -o ../log/testreport/html'))
    logging.info("End to execute APP UI automaction cases")
