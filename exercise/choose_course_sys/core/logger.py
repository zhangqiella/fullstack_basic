# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/1
@File: logger.py
'''

import logging
from config import setting


def logger(logger_type):

    logger = logging.getLogger(logger_type)
    logger.setLevel(setting.LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setLevel(setting.LOG_LEVEL)

    log_file_name = '.'.join([logger_type,'log'])
    log_file_path = '\\'.join([setting.LOG_PATH, log_file_name])
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(setting.LOG_LEVEL)

    fmt = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(filename)s - %(lineno)d - %(message)s')
    ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger