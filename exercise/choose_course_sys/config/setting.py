# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/1
@File: setting.py
'''

import logging
import os


ROLE = {
    'student': {},
    'teacher': {},
    'administrator': {}}

DB_BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db')
DB_PATH_SCHOOL = os.path.join(DB_BASE_PATH, 'school')
DB_PATH_COURSE = os.path.join(DB_BASE_PATH, 'course')
DB_PATH_CLASSROOM = os.path.join(DB_BASE_PATH, 'classroom')
DB_PATH_TEACHER = os.path.join(DB_BASE_PATH, 'teacher')
DB_PATH_ADMIN = os.path.join(DB_BASE_PATH, 'administrator')
DB_PATH_STUDENT = os.path.join(DB_BASE_PATH, 'student')
DB_PATH_COURSE_TO_TEACHER = os.path.join(DB_BASE_PATH, 'course_to_teacher')
DB_PATH_STUDENT_ACCOUNT = os.path.join(DB_BASE_PATH, 'account','student')
DB_PATH_TEACHER_ACCOUNT = os.path.join(DB_BASE_PATH, 'account','teacher')




BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_PATH, 'log')
LOG_LEVEL = logging.DEBUG