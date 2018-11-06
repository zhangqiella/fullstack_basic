# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/1
@File: student.py
'''
import os, sys
searchpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(searchpath)

from core import student_main

if __name__ == '__main__':
    student_main().run()

