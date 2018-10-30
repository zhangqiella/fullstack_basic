# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: atm.py
'''
import os
import sys
atm_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(atm_path)

from core.atm_module import atmmain

def run():
    atmmain.main()

if __name__ == '__main__':
    run()