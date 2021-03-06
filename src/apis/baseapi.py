#! /usr/bin/env python
# coding=utf-8

import logging
import requests
from initialization.sysconfig import sys_cfg


class BaseAPI:

    def __init__(self):
        logging.info("init base api interface")
        self.corp_id = sys_cfg.get('corp_para', 'corp_id')
        self.token_url = sys_cfg.get('corp_para', 'token_url')
        logging.info("corp_id=" + self.corp_id)


    def get_token(self, secret):

        params = {'corpid': self.corp_id, 'corpsecret': secret}
        logging.info('params' + str(params))
        logging.info('token_url:' + self.token_url)
        token_res = requests.get(self.token_url, params=params)

        return token_res.json().get('access_token')

    def post_json(self, url, json_obj, params=None):
        if params:
            self.res = requests.post(url, json=json_obj, params=params)
        else:
            self.res = requests.post(url, json=json_obj)

    def get_response(self):
        return self.res.json()
