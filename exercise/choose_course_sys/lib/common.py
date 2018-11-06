# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/2
@File: common.py
'''

import uuid
import hashlib


def create_uuid():
    UID = uuid.uuid1()
    return str(UID)

#作用：把password算成md5的值，然后存在数据文件中，
#这样即使数据文件被获取，也不能马上获得用户密码
def pwd_md5(input_str):
    md5 = hashlib.md5()
    md5.update(input_str)
    return md5.hexdigest()

def test():
    pass

if __name__ == '__main__':
    test()