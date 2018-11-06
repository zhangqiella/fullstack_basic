# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/5
@File: test.py
'''


def makebold(fn):
    def wrapper():
        print(123)
        return "<b>" + fn() + "</b>"

    return wrapper


def makeitalic(fn):
    def wrapper():
        print(456)
        return "<i>" + fn() + "</i>"

    return wrapper


@makebold
@makeitalic
def hello():
    print('hello')
    return "hello alvin"


(hello()