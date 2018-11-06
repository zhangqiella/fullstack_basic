# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/1
@File: administrator.py
'''

import os, sys

search_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(search_path)

from core import admin_main

if __name__ == '__main__':
    admin_main.run()