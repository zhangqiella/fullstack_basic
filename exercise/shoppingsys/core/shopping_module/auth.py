# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: auth.py
'''


import json
import os
import time
import core.shopping_module.main
from log import logger
from config import setting
from core.shopping_module import main


def auth_file(logger_obj):
    try_time = 0
    while try_time < 3:
        account = input('please input the account name:').strip()
        password = input('please input the account password').strip()

        db_path = setting.DATABASE['path']
        file_path = os.path.join(db_path,'.'.join([account,'json']))
        #由于windows下文件名不区分大小写，所以，如果认为大小写不同，需要再检查一遍id
        if os.path.isfile(file_path):
            with  open(file_path,'r') as fh:
                data1 = fh.read()
                ###之前我写成data.loads()错了！！！
                data = json.loads(data1)
                if data['id'] == account and data['password'] == password:
                    expire_time = data['expire_date']
                    expire_time = time.mktime(time.strptime(expire_time,'%Y-%m-%d'))
                    current_time = time.time()
                    if current_time < expire_time:
                        return True
                    else:
                        logger_obj.warning('expired!')
                        return False
                else:
                    try_time += 1
                    logger_obj.warning('incorrect account name or password, you still have %d more attempts'%(3-try_time))

        else:
            try_time +=1
            logger_obj.warning('incorrect account name or password, you still have %d more attempts' % (3-try_time))

    else:
        logger_obj.warning('you have too many attempts')
        return False


def auth_sql(account, password, logger_obj):
    pass

def login(func):
    def inner(*args, **kwargs):
        if main.shop_user_data['is_authenticated'] == True:
            return func(*args, **kwargs)
        else:
            ###获取参数的方法重要
            args[0].warning('No authentication.You must login first!!')
            auth_result = auth_account(args[0])
            if auth_result:
                main.shop_user_data['is_authenticated'] = True
                args[0].info('login passed!')
                return func(*args, **kwargs)
            else:
                args[0].warning('log failed!')
                exit()
    return inner

#要考虑数据存储在数据库和文件里的两种情况。
def auth_account(logger_obj):
    auth_data = {
        'file_storage': auth_file,
        'sql': auth_sql
    }

    #不同的数据存储方式，对应不同的auth方法，
    storage_style = setting.DATABASE['engine']
    auth_result = auth_data[storage_style](logger_obj)

    return auth_result