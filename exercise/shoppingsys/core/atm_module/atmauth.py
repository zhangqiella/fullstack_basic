# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: auth.py
'''

import os
import time

from core.atm_module import atmmain
from core.atm_module import db_handler
from config import setting

def atmlogin(func):
    def inner(*args, **kwargs):
        if atmmain.atm_user_data['is_authenticated'] == False:
            atmmain.atm_logger.warning('no authenticated,input your username and password to log in!')
            if atm_auth():
                atmmain.atm_user_data['is_authenticated'] = True
                atmmain.atm_logger.warning('log in passed!')
                return func(*args, **kwargs)
            else:
                atmmain.atm_logger.warning('login failed!')
                exit()
        else:
            atmmain.atm_logger.debug('has logged in!')
            return func(*args, **kwargs)
    return inner

#从文件冲读取db鉴权过程
def atm_auth_file():
    try_time = 0
    acc_data = None
    while try_time < 3:
        account = input('pls input atm user name:').strip()
        password = input('pls input atm user password:').strip()
        acc_data = db_handler.dbhandler(account)
        if acc_data:
            if acc_data['id'] == account and acc_data['password'] == password:
                expire_time = acc_data['expire_date']
                expire_time = time.mktime(time.strptime(expire_time, '%Y-%m-%d'))
                current_time = time.time()
                if expire_time > current_time:
                    atmmain.atm_logger.warning('log passed!')
                    atmmain.atm_user_data['user_name'] = acc_data['id']
                    atmmain.atm_user_data['acc_data'] = acc_data
                    return True
                else:
                    atmmain.atm_logger.warning('time expiration!')
                    return False
            else:
                try_time += 1
                atmmain.atm_logger.warning('incorrect atm username and password')
                atmmain.atm_logger.warning('you still have %d times to try' % (3 - try_time))
        else:
            try_time += 1
            atmmain.atm_logger.warning('incorrect atm username and password')
            atmmain.atm_logger.warning('you still have %d times to try'%(3-try_time))
    else:
        return False

def atm_auth_sql():
    pass

def atm_auth():

    atm_auth_func = {
        'file_storage':atm_auth_file,
        'sql':atm_auth_sql
    }

    atm_auth_ret = atm_auth_func[setting.ATMDB['engine']]()

    return atm_auth_ret

def test():
    pass
if __name__ =='__main__':
    test()