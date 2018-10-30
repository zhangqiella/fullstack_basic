# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: shopping.py
'''
import os
import sys
# 动态添加的，所以会有红线


shop_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#windows 中，连接路径时要用两个斜杠\\
# shop_dir = '\\'.join([shop_dir,'core'])
# print('the base direction of shopping is', shop_dir)
sys.path.append(shop_dir)
# print(sys.path)

#这步import要再sys.path路径操作完之后
from core.shopping_module import main


if __name__=='__main__':
    main.main()
