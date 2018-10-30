# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: db_handler.py
'''
import os
import json
from config import setting

def file_db_handle(account_id):
    file_path = os.path.join(setting.ATMDB['path'], '.'.join([account_id,'json']))
    if os.path.isfile(file_path):
        with open(file_path,'r') as fh:
            data1 = fh.read()
            data = json.loads(data1)
        return data
    else:
        return None

def sql_db_handle(filename,action_type):
    pass

def dbhandler(filename):
    if setting.ATMDB['engine'] == 'file_storage':
        return file_db_handle(filename)

    elif setting.ATMDB['engine'] == 'sql':
        return sql_db_handle(filename)

    else:
        print('please note the db way')


def test():
    pass

if __name__ == '__main__':
    test()