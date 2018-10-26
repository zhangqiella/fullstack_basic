# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/26
@File: caculation.py
'''

import re
import logging
from logging import handlers

#check if the string is legal
def check_expr(s):
    check_status = True
    if not s.count('(') == s.count(')'):
        logger.warning("括号未闭合")
        check_status = False
    if re.findall('[^0-9]+-*/.()]', s):
        check_status = False
    return check_status

def str_format(s):
    s = s.replace(' ','')
    s = s.replace('++',"+")
    s = s.replace('+-',"-")
    s = s.replace('--', "+")
    s = s.replace('-+', '-')
    s = s.replace('*+','*')
    s = s.replace('/+','/')

    return s

def multi_div_calc(s):
    while re.findall('[*/]',s):
        multi_div_1st = re.search('[+-]?\d+\.?\d*([*/]|\*\*)[+-]?\d+\.?\d*',s).group()
        multi_or_div = re.search('[*/]',multi_div_1st).group()

        if multi_or_div == '*':
            for_mul_div = re.split('\*', multi_div_1st)
            result = float(for_mul_div[0])*float(for_mul_div[1])

        elif multi_or_div == '/':
            for_mul_div = re.split('/', multi_div_1st)
            result = float(for_mul_div[0])/float(for_mul_div[1])

        str_result = '+' + str(result)
        s = s.replace(multi_div_1st, str_result)
        s = str_format(s)
    return s

def add_minus_calc(s):
    add_object = '[-]?\d+\.?\d*\+[+-]?\d+\.?\d*'
    minus_object = '[-]?\d+\.?\d*\-[+-]?\d+\.?\d*'
    #20-30+40+50-60   +40+50
    while re.findall(add_object,s):
        add_1st = re.search(add_object,s).group()
        for_add = re.split('\+', add_1st)
        add_result = float(for_add[0]) + float(for_add[1])

        str_result = '+' + str(add_result)
        s = s.replace(add_1st, str_result)
        s = str_format(s)
    while re.findall(minus_object,s):
        minus_1st = re.search(minus_object,s).group()
        for_minus = re.split('\-',minus_1st)
        if len(for_minus) == 3:
            minus_result = 0
            for v in for_minus:
                if v:
                    minus_result -= float(v)
        else:
            minus_result = float(for_minus[0]) - float(for_minus[1])

        str_result = '+' + str(minus_result)
        s = s.replace(minus_1st, str_result)
        s = str_format(s)

    return s


if __name__=='__main__':

#引入log相关
#实现同时在屏幕和文件中打印log
#文件中的log bkup，最多backup3个log文件，旧的自动删除

    logger = logging.getLogger('calcu_log')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # fh = logging.FileHandler('caculation.log')
    logfile_name = 'calc_log.log'
    fh = handlers.TimedRotatingFileHandler(filename=logfile_name, when='S', interval=5, backupCount=3)
    fh.setLevel(logging.DEBUG)

    fmt=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

    source = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)) '
    #直接计算的结果，供比较
    #result = eval(source)
    to_calc = str_format(source)
    if check_expr(to_calc):
        while re.findall('\(',to_calc):
            logger.debug("expression for calc is %s"%to_calc)
            in_bracket = re.search('\([^()]+\)',to_calc).group()
            s_after_multi_div = multi_div_calc(in_bracket)
            s_after_add_minus = add_minus_calc(s_after_multi_div)
            logger.debug('expression %s after calc is %s'%(in_bracket,s_after_add_minus))
            to_calc = to_calc.replace(in_bracket,s_after_add_minus[1:-1])
            logger.debug('now the expression are %s'%to_calc)

        else:
            s_after_multi_div = multi_div_calc(to_calc)
            s_after_add_minus = add_minus_calc(s_after_multi_div)
            to_calc = to_calc.replace(to_calc, s_after_add_minus)
            logger.debug("the result is:%s"%to_calc)
    else:
        logger.warning('Illegal expression')