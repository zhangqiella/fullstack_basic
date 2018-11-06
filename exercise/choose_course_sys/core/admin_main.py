# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/11/1
@File: admin_main.py
'''


import os, pickle
from core import models
from core import logger
from lib import common
from core import identify
from config.setting import DB_PATH_ADMIN

admin_logger = logger.logger('admin')
is_authenticated = False
db_path = DB_PATH_ADMIN


def login(func):
    def inner():
        # 这个global声明必须在inner函数里
        global is_authenticated
        try_time = 0
        while try_time < 3:
            if is_authenticated:
                return func()
            else:
                try_time += 1
                username = input('请输入用户名：').strip()
                password = input('请输入密码').strip()
                for file in os.listdir(db_path):
                    file_dir = os.path.join(db_path, file)
                    data = pickle.load(open(file_dir, 'rb'))
                    if data.name == username and data.pwd == password:
                        is_authenticated = True
                        print('login succeed')
                    else:
                        if try_time != 3:
                            print('login failed, re-login %d times left' % (3 - try_time))
                        else:
                            print('login failed')
    return inner


def create_school():
    add_flag = True
    while add_flag:
        school_name = input('输入学校名称：').strip()
        # 需增加对school _name的检查，是否已经存在这个学校，存在则不可以添加
        school_city = input('输入学校所在城市：').strip()
        new_school = models.School(school_name, school_city)
        admin_logger.warning('create a school ')
        '''调用db接口，修改school的存储的数据，增加这个学校'''

        ret = new_school.storage()
        if ret:
            admin_logger.warning('insert db 成功 ')
        else:
            admin_logger.warning('insert db 失败 ')

        continue_flag = input('do you want to continue to add school y/n').strip()
        if continue_flag == 'n':
            add_flag = False

    return new_school


def delete_school():
    pass


def modify_school():
    pass


def get_school():
    school_list = models.School.get_all_list()


def create_classroom():
    school_list = models.School.get_all_list()

    add_flag = True
    while add_flag:

        for number,school_obj in enumerate(school_list,1):
            print(number, '>>>>', school_obj.name)

        school_index = input('选择班级所在的学校').strip()
        school_nid = school_list[int(school_index)-1].nid

        # 这里需要判断输入合理性
        classroom_name = input('输入班级名称：').strip()
        new_classroom = models.Classroom(classroom_name, school_nid)

        admin_logger.warning('create a classroom ')
        '''调用db接口，修改course的存储的数据，增加这个课程'''

        ret = new_classroom.storage()

        if ret:
            admin_logger.warning('insert db 成功 ')
        else:
            admin_logger.warning('insert db 失败 ')

        continue_flag = input('do you want to continue to add classroom y/n').strip()
        if continue_flag == 'n':
            add_flag = False

    return new_classroom


def delete_classroom():
    pass


def modify_classroom():
    pass


def create_teacher():
    school_list = models.School.get_all_list()

    add_flag = True
    while add_flag:
        teacher_name = input('输入创建讲师姓名：').strip()
        print('学校list：')
        for number, school_obj in enumerate(school_list, 1):
            print(number, '>>>>', school_obj.name)

        school_index = input('选择讲师所属学校').strip()
        school_nid = school_list[int(school_index) - 1].nid

        # 这里需要判断输入合理性
        new_teacher = models.Teacher(teacher_name, school_nid)
        admin_logger.warning('create a teacher ')
        '''调用db接口，修改course的存储的数据，增加这个课程'''

        ret = new_teacher.storage()

        if ret:
            admin_logger.warning('insert db 成功 ')
        else:
            admin_logger.warning('insert db 失败 ')

        continue_flag = input('do you want to continue to add teacher y/n').strip()
        if continue_flag == 'n':
            add_flag = False

    return new_teacher


def create_student():
    school_list = models.School.get_all_list()

    add_flag = True
    while add_flag:
        student_name = input('请输入所创建学生名字：').strip()
        student_gender = input('请输入性别：').strip()

        for number,school_obj in enumerate(school_list,1):
            print(number,'>>>>', school_obj.name)
        school_index = input('选择学生所在的学校').strip()
        school_nid = school_list[int(school_index)-1].nid
        classroom_list = models.Classroom.get_classroom_list_by_school_id(school_nid)

        for number, classroom_obj in enumerate(classroom_list,1):
            print(number,'>>>>', classroom_obj.name)
        classroom_index = input('选择学生所属班级').strip()
        classroom_nid = classroom_list[int(classroom_index)-1].nid

        new_student = models.Student(student_name, student_gender, school_nid, classroom_nid)

        admin_logger.warning('create a student ')
        '''调用db接口，修改course的存储的数据，增加这个学生'''

        ret = new_student.storage()

        if ret:
            admin_logger.warning('insert db 成功 ')
        else:
            admin_logger.warning('insert db 失败 ')

        continue_flag = input('do you want to continue to add student y/n').strip()
        if continue_flag == 'n':
            add_flag = False


def create_course():
    print('请选择所属学校')
    school_list = models.School.get_all_list()

    add_flag = True
    while add_flag:
        for number, school_obj in enumerate(school_list, 1):
            print(number, '>>>>', school_obj.name)
        school_index = input('选择课程所在的学校').strip()
        school_nid = school_list[int(school_index)-1].nid

        # 这里需要判断输入合理性
        course_name = input('输入课程名称：').strip()
        course_period = input('课程的周期').strip()
        course_price = input('课程的价钱').strip()

        new_course = models.Course(course_name, school_nid, course_period, course_price)
        admin_logger.warning('create a course ')
        '''调用db接口，修改course的存储的数据，增加这个课程'''

        ret = new_course.storage()

        if ret:
            admin_logger.warning('insert db 成功 ')
        else:
            admin_logger.warning('insert db 失败 ')

        continue_flag = input('do you want to continue to add course y/n').strip()
        if continue_flag == 'n':
            add_flag = False

    return new_course


def create_course_to_teacher():
    add_flag = True
    while add_flag:
        course_list = models.Course.get_all_list()
        for index, course_obj in enumerate(course_list, 1):
                school_obj = course_obj.school_nid.get_obj_by_uuid()
                print(index,'>>>>', course_obj.name, school_obj.name, course_obj.period, course_obj.price)
        course_index = input('选择课程').strip()

        course_id = course_list[int(course_index)-1].nid
        school_id = course_list[int(course_index)-1].school_nid

        teacher_list = models.Teacher.get_teacher_by_school_id(school_id)
        for index, teacher_obj in enumerate(teacher_list, 1):
            print(index, '>>>>>>', teacher_obj.name)

        teacher_index = input('选择该课程老师').strip()
        teacher_id = teacher_list[int(teacher_index) - 1].nid

        new_obj = models.CourseToTeacher(course_id, teacher_id)

        new_obj.storage()

        continue_flag = input('do you want to continue to add course y/n').strip()
        if continue_flag == 'n':
            add_flag = False

    return new_obj

'''管理员的主程序，先输入操作对象，选择，学校，班级，课程，输入q退出，
然后输入具体操作create/delete/modify/get,增删改查操作，b返回上一层菜单
'''


@login
def run():
    while True:
        print('欢迎进入选课系统')
        print_info = '''----选择操作的目标-----
        ------you can enter 'q' to quit
       1. 学校
       2. 班级
       3. 课程
       4. 讲师
       5. 学生
       6. 课程老师表
       q for quit
       '''

        print(print_info)

        menu_dict = {'1': {'create': create_school, 'delete': delete_school, 'modify': modify_school,'get': get_school},
                     '2': {'create': create_classroom,'delete': delete_classroom,'modify':modify_classroom},
                     '3': {'create': create_course},
                     '4': {'create': create_teacher},
                     '5': {'create': create_student},
                     '6':{'create': create_course_to_teacher}}

        input_index = input('please input the item you want to take action:').strip()
        if input_index == 'q':
            exit(0)
        elif input_index in menu_dict.keys():
            print_info = '''----选择操作-----
                    ------you can enter 'b' to back to main menu
                   create
                   delete
                   modify
                   get
                   '''
            input_action = input('input the action you want to take create/delete/modify/get:').strip()
            if input_action == 'b':
                continue
            elif input_action in menu_dict[input_index].keys():
                ret = menu_dict[input_index][input_action]()
                print(ret)
        else:
            admin_logger.warning('invalid input for administrator action ')


def test():
    pass


if __name__ == '__main__':
    test()