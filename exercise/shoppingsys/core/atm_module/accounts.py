# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: accounts.py
'''

import json
import os
from config import setting
from core.atm_module import db_handler

def loaddata(accountid):
    acc_data = db_handler.dbhandler(accountid)
    return acc_data

def dumpdata(acc_data):
    file_path = os.path.join(setting.ATMDB['path'], '.'.join([acc_data['id'], 'json']))
    if os.path.isfile(file_path):
        with open(file_path, 'w') as fh:
            data = json.dump(acc_data, fh)
        return data

def test():
    pass

if __name__ == '__main__':
    test()