# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: transaction.py
'''

from config import setting
from core.atm_module import accounts

def make_transaction(money,trans_type, acc_data, logger_obj):
    action = setting.TRANSACTION_TYPE[trans_type]['action']
    interest = setting.TRANSACTION_TYPE[trans_type]['interest']

    if action == 'minus':
        new_balance = acc_data['balance'] - money
        if new_balance < 0:
            return None
        else:
            acc_data['balance'] = new_balance
    elif action == 'plus':
        new_balance = acc_data['balance'] + money
        acc_data['balance'] = new_balance
    else:
        pass

    accounts.dumpdata(acc_data)
    return acc_data

def test():
    pass
if __name__ == '__main__':
    test()