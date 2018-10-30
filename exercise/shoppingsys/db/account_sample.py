# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: account_sample.py
'''


import json
import os
acc_dic = {
    'id': 'liyong',
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2018-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

data = json.dumps(acc_dic)

basename = os.path.dirname(os.path.abspath(__file__))
shop_data_path = '\\'.join([basename, 'shop_user_repo'])

if not os.path.exists(shop_data_path):
    os.mkdir(shop_data_path)

shop_user_file_name = '.'.join([acc_dic['id'],'json'])
shop_data_path = '\\'.join([basename, 'shop_user_repo',shop_user_file_name])

fh = open(shop_data_path, 'w')
fh.write(data)
fh.close()