# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/2
@File: models.py
'''
import pickle,os
from config import setting
from core import identify
from lib import common


class BaseClass:
    #定义的class school teacher course类都有储存操作，所以提取出来一个base类，里面有storage操作就可以了。
    #当任意class school teacher course对象调用storage时，会把obj的所有name等字段带着来调用这个函数
    #另外，对于db_path，class school teacher course每个类各有一个路径，并不是每个对象有一个，所以提取出来一个静态字段。
    #静态字段可以用类调用，也可以用对象调用

    def storage(self):
        data = pickle.dumps(self)

        if not os.path.isdir(self.db_path):
            os.mkdirs(self.db_path)
        fh = open(os.path.join(self.db_path, self.nid.uuid), 'wb')
        ret = fh.write(data)
        fh.close()

        return ret


class Admin(BaseClass):
    db_path = setting.DB_PATH_ADMIN

    def __init__(self, name, password):
        self.nid = identify.AdminNid(Admin.db_path)
        self.name = name
        self.pwd = password


class School(BaseClass):
    db_path = setting.DB_PATH_SCHOOL

    def __init__(self, name, city):
        self.nid = identify.SchoolNid(School.db_path)
        self.name = name
        self.city = city
        self.classroom =[]
        self.teacher = []
        self.student = []
        self.course = []

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_city(self):
        return self.city

    def set_city(self,new_city):
        self.city = new_city

    def update_classroom(self, item, action):
        if action == 'add':
            self.classroom.append(item)
        elif action == 'delete':
            self.classroom.pop(item)
        else:
            pass

    @staticmethod
    def get_all_list():
        ret_obj = []
        for item in os.listdir(School.db_path):
            file_path = os.path.join(School.db_path,item)
            fh = open(file_path, 'rb')
            obj = pickle.loads(fh.read())
            fh.close()

            ret_obj.append(obj)
        return ret_obj


class Course(BaseClass):
    db_path = setting.DB_PATH_COURSE

    def __init__(self, name, school_nid, period, price):
        self.nid = identify.CourseNid(Course.db_path)
        self.name = name
        self.school_nid = school_nid
        self.period = period
        self.price = price

    @staticmethod
    def get_all_list():
        ret_obj = []
        for item in os.listdir(Course.db_path):
            file_path = os.path.join(Course.db_path,item)
            fh = open(file_path, 'rb')
            obj = pickle.loads(fh.read())
            fh.close()

            ret_obj.append(obj)
        return ret_obj


class Student(BaseClass):
    db_path = setting.DB_PATH_STUDENT

    def __init__(self, name, gender, school_nid, classroom_nid):
        self.nid = identify.StudentNid(Student.db_path)
        self.name = name
        self.gender = gender
        self.school_nid = school_nid
        self.classroom_id = classroom_nid


class Teacher(BaseClass):
    db_path = setting.DB_PATH_TEACHER

    def __init__(self, name, school_nid):
        self.nid = identify.TeacherNid(Teacher.db_path)
        self.name = name
        self.school_nid = school_nid

    @staticmethod
    def get_all_list():
        ret_obj = []
        for item in os.listdir(Teacher.db_path):
            file_path = os.path.join(Teacher.db_path,item)
            fh = open(file_path, 'rb')
            obj = pickle.loads(fh.read())
            fh.close()

            ret_obj.append(obj)
        return ret_obj

    @staticmethod
    def get_teacher_by_school_id(school_id):
        ret_obj = []
        for item in os.listdir(Teacher.db_path):
            file_path = os.path.join(Teacher.db_path, item)
            fh = open(file_path, 'rb')
            obj = pickle.loads(fh.read())
            fh.close()

            if obj.school_nid.uuid == school_id.uuid:
                ret_obj.append(obj)
        return ret_obj


class CourseToTeacher(BaseClass):
    db_path = setting.DB_PATH_COURSE_TO_TEACHER

    def __init__(self, course_nid, teacher_nid):
        self.nid = identify.CourseToTeacherNid(CourseToTeacher.db_path)
        self.course_nid = course_nid
        self.teacher_nid = teacher_nid


class Classroom(BaseClass):
    db_path = setting.DB_PATH_CLASSROOM

    def __init__(self, name, school_nid, course_list=[], teacher_list=[]):
        self.nid = identify.ClassroomNid(Classroom.db_path)
        self.name = name
        self.school_nid = school_nid
        self.courses = course_list
        self.teachers = teacher_list

    def modify_school_list(self):
        pass

    def modify_teacher_list(self):
        pass

    @staticmethod
    def get_all_classroom_list():
        pass

    @staticmethod
    def get_classroom_list_by_school_id(school_id):
        ret_obj = []
        print('get_classroom', school_id)
        for item in os.listdir(Classroom.db_path):
            file_path = os.path.join(Classroom.db_path, item)
            fh = open(file_path, 'rb')
            obj = pickle.loads(fh.read())
            fh.close()
            if obj.school_nid.uuid == school_id.uuid:
                ret_obj.append(obj)
        return ret_obj


class AdminLogin:
    def __init__(self, func):
        print('login init')
        self._func = func
        self.is_authenticated = False
        pass

    def __call__(self):
        try_time = 0
        while try_time < 3:
            if self.is_authenticated:
                self._func()
            else:
                username = input('请输入用户名：').strip()
                password = input('请输入密码').strip()
                for file in os.listdir(setting.DB_PATH_ADMIN):
                    file_dir = os.path.join(setting.DB_PATH_ADMIN, file)
                    data = pickle.load(open(file_dir, 'rb'))
                    if data.name == username and data.pwd == password:
                        self.is_authenticated = True
                        print('login succeed')
                    else:
                        print('login failed, re-login %d times left' % (2 - try_time))
                        try_time += 1


class StudentAccount(BaseClass):
    db_path = setting.DB_PATH_STUDENT_ACCOUNT

    def __init__(self, username, password, student_nid):
        self.nid = identify.StudentAccountNid(StudentAccount.db_path)
        self.username = username
        self.password = password
        self.student_nid = student_nid


class TeacherAccount(BaseClass):
    db_path = setting.DB_PATH_TEACHER_ACCOUNT

    def __init__(self, username, password, teacher_nid):
        self.nid = identify.TeacherAccountNid(TeacherAccount.db_path)
        self.username = username
        self.password = password
        self.teacher_nid = teacher_nid


def test():
    pass


if __name__ == '__main__':
    test()