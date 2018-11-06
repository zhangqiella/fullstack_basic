# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/6
@File: create_accounts.py
'''
import os,pickle
from core import models
from config import setting
from core import models
# 根据目前admin添加的student和teacher给他们生成相应的账号的工具


def create_account(role):
    if role == 'student':
        db_path = setting.DB_PATH_STUDENT
    elif role == 'teacher':
        db_path = setting.DB_PATH_TEACHER
    else:
        raise Exception('用户角色定义错误')

    for item in os.listdir(db_path):
        file_dir = os.path.join(db_path, item)
        fh = open(file_dir, 'rb')
        data = pickle.load(fh)
        fh.close()
        school_name = data.school_nid.get_obj_by_uuid().name
        username = '_'.join([data.name, school_name])
        password = '123456'

        if role == 'student':
            new_student_account = models.StudentAccount(username, password, data.nid)
            new_student_account.storage()
        else:
            new_teacher_account =models.TeacherAccount(username, password, data.nid)
            new_teacher_account.storage()


def show_accounts(role):
    if role == 'student':
        db_path = setting.DB_PATH_STUDENT_ACCOUNT
    elif role == 'teacher':
        db_path = setting.DB_PATH_TEACHER_ACCOUNT
    else:
        raise Exception('用户角色定义错误')

    for item in os.listdir(db_path):
        file_dir = os.path.join(db_path, item)
        fh = open(file_dir, 'rb')
        data = pickle.load(fh)
        print(data.username, data.password)

def test():
    # create_account('teacher')
    show_accounts('student')
    show_accounts('teacher')

if __name__ == '__main__':
    test()