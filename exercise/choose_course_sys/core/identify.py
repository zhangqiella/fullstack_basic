# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/2
@File: identify.py
'''
import os,pickle
from lib import common


class Nid:
    def __init__(self, role, db_path):
        role_list = ['admin', 'student', 'teacher', 'course', 'classroom', 'school',
                     'course_to_teacher','student_account', 'teacher_account']
        if role in role_list:
            self.role = role
        else:
            raise Exception('用户角色定义错误，选项为：%s' % ','.join(role_list))
        self.db_path = db_path
        self.uuid = common.create_uuid()
    # 每个nid 对象有成员uuid,db_load,role.可以由nid的uuid，获取相应的对象。比如可以由school_nid获取school对象。
    # student_nid 获取student对象，但是不可以由student nid获取school对象，这种获取需要另外写函数
    def get_obj_by_uuid(self):
        for name in os.listdir(self.db_path):
            if name == self.uuid:
                return pickle.load(open(os.path.join(self.db_path, name), 'rb'))


class AdminNid(Nid):
    def __init__(self,db_path):
        super(AdminNid,self).__init__('admin', db_path)


class TeacherNid(Nid):
    def __init__(self,db_path):
        super(TeacherNid,self).__init__('teacher', db_path)


class ClassroomNid(Nid):
    def __init__(self,db_path):
        super(ClassroomNid,self).__init__('classroom', db_path)


class StudentNid(Nid):
    def __init__(self, db_path):
        super(StudentNid,self).__init__('student', db_path)


class CourseNid(Nid):
    def __init__(self, db_path):
        super(CourseNid,self).__init__('course', db_path)


class SchoolNid(Nid):
    def __init__(self, db_path):
        super(SchoolNid,self).__init__('school', db_path)


class CourseToTeacherNid(Nid):
    def __init__(self, db_path):
        super(CourseToTeacherNid,self).__init__('course_to_teacher', db_path)


class StudentAccountNid(Nid):
    def __init__(self, db_path):
        super(StudentAccountNid, self).__init__('student_account', db_path)


class TeacherAccountNid(Nid):
    def __init__(self, db_path):
        super(TeacherAccountNid, self).__init__('teacher_account', db_path)

def test():
    pass


if __name__ == '__main__':
    test()