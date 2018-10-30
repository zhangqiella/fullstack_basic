# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: setting.py
'''
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

##path里的分隔符要注意，在windows和linux系统下不同！！！
DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s\db\shop_user_repo" % BASE_DIR
}

ATMDB = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s\db\\atm_user_repo" % BASE_DIR
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}

LOGLEVEL = logging.DEBUG