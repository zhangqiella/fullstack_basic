# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: logger.py
'''

import os
import logging
from config import setting

def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(setting.LOGLEVEL)

    log_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = "\\".join([log_dir,'log'])
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_file = '\\'.join([log_dir, log_type])
    ch = logging.StreamHandler()
    fh = logging.FileHandler(log_file)

    #格式要有logging。Formatter这一步，直接把format的格式字符串传入setFormatter错误！！
    fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')

    ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

if __name__=='__main__':
    test_logger = logger('test_log')
    test_logger.debug('test log hello')

