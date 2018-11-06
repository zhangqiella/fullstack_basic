# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/5
@File: initialize.py
'''
import os,sys

search_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(search_path)

from core import models

def main():
    admin_name = input('输入管理员账户：').strip()
    admin_pwd = input('输入管理员密码：').strip()
    new_admin = models.Admin(admin_name, admin_pwd)
    new_admin.storage()

def test():
    pass


if __name__ == '__main__':
    main()