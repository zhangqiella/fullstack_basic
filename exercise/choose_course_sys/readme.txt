本来我的代码组织形式是
--admin_main.py                        定义了administrator角色视图发起的操作
--school_main.py 里面定义了school类
--student_main.py 里面定义了student类，以及student角色视图发起的操作
--teacher_main.py 里面定义了teacher类，以及teacher的角色视图发起的操作
--course_main.py 里面定义了course类
--classroom_main.py   里面定义了classroom类，
--db_handler.py


而示例代码的组织形式，把所有类定义放在了一个文件里，叫做model。
而course，teacher，classroom是不会主动发起操作的
所以示例代码较好。

每个角色发起的操作，各定义一个文件。
--admin_main.py   定义了administrator角色视图发起的操作
--student_main.py 定义了student角色视图发起的操作
--teacher_main.py 定义了teacher的角色视图发起的操作
--model.py        定义了school, student, teacher,classroom, course类。

PEP的一些规范，不符合规范，会有灰色下划线

比如最外层函数，类定义，前面空两行
里面一层的函数等定义，前面空一行
，后面跟一个空格
类的命名，驼峰式命名

注释行，#后空一个空格


1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校，
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里

1，创建上海校区，北京校区
2，上海校区，创建全栈1班，全栈2班，北京校区创建全栈1班，全栈2班，全栈3班
3，课程，上海校区，go，linux。 北京校区，linux，python
4, 老师，上海校区，tandde，micheal，amanda 北京校区Cody， tracy，alex
5，学生，ethan,ryan,bob,pony上海全栈1班
barack，helen，上海全栈2班
ellen,julian，sara北京全栈3班
jack,pony,北京全栈2班
desmond,小明 北京全栈1班

linux 北京校区 tracy
python 北京校区 alex
linux 上海校区  amanda
go 上海校区  tandde

用tool的create_accounts根据目前有的学生生成了账号，密码：
jack_北京校区 123456
desmond_北京校区 123456
pony_上海校区 123456
小明_北京校区 123456
pony_北京校区 123456
ethan_上海校区 123456
ryan_上海校区 123456
bob_上海校区 123456
helen_上海校区 123456
barack_上海校区 123456
ellen_北京校区 123456
julian_北京校区 123456
sara_北京校区 123456
tandde_上海校区 123456
micheal_上海校区 123456
amanda_上海校区 123456
cody_北京校区 123456
tracy_北京校区 123456
alex_北京校区 123456


目前实现了：administrator的登录，create 学员，课程，讲师，班级，学校功能



