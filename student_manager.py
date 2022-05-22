import file_manager
import model

name = ''
students = []  # 存放添加的学生信息


def add_student():
    while True:
        stu_name = input('请输入学生姓名:')
        stu_age = input('请输入年龄:')
        stu_gender = input('请输入性别:')
        stu_tel = input('请输入电话:')

        s = model.Student(stu_name, stu_age, stu_gender, stu_tel)  # 创建一个Student对象
        students.append(s.__dict__)  # 将学生对象 s 转化成字典添加到列表students中
        data = {'all_student': students, 'num': len(students)}
        # data里面的存放的数据形式：{
        #                           'all_student':[
        #                               {'name':'Lisa', 'age':18, 'gender':'女', 'tel':'123456'}
        #                               {'name':'Lisa', 'age':18, 'gender':'女', 'tel':'123456'}
        #                                        ]
        #                       }
        choice = input('添加成功！\n1.添加\n2.返回\n请选择(1-2):')
        if choice == '2':
            break


def show_student():
    operator = input('1.查看所有学生信息\n2.根据姓名查找\n其他:返回\n请选择:')
    if operator == '1':
        for student in students:
            print('姓名:{name},年龄:{age},性别:{gender},电话:{tel}'.format(**student))
    elif operator == '2':
        stu_name = input('请输入学员名字:')
        same_stu_name = []  # 可能有重名  存储要查找的学生信息
        for student in students:
            if student['name'] == stu_name:
                same_stu_name.append(student)
            for student in same_stu_name:
                print('姓名:{name},年龄:{age},性别:{gender},电话:{tel}'.format(**student))
    else:
        return


def modify_student():
    m_name = input('请输入要修改学生的姓名:')
    for student in students:
        if m_name == student['name']:
            while True:
                operator = input('1.修改此学生的姓名\n2.修改此学生的年龄\n3.修改此学生的性别\n4.修改此学生的电话\n5.返回\n请选择(1-5):')
                if operator == '1':
                    new_name = input('请输入新的名字:')
                    student['name'] = new_name
                    print('修改成功！')
                    break
                elif operator == '2':
                    new_age = input('请输入新的年龄:')
                    student['age'] = new_age
                    print('修改成功！')
                    break
                elif operator == '3':
                    new_gender = input('请输入新的性别:')
                    student['gender'] = new_gender
                    print('修改成功！')
                    break
                elif operator == '4':
                    new_tel = input('请输入新的电话:')
                    student['tel'] = new_tel
                    print('修改成功！')
                    break
                elif operator == '5':
                    return
                else:
                    print('输入有误！')
                    break
    else:
        print('你要修改的学生不存在！')


def delete_student():
    operator = input('1.按名字删除\n2.返回\n请选择:')
    if operator == '1':
        del_name = input('请输入要删除的学生的名字:')
        for student in students:
            if del_name == student['name']:
                students.remove(student)
    elif operator == '2':
        return
    else:
        print('输入有误！')


def show_manager():
    # print('显示管理页面')
    content = file_manager.read_file('students_page.txt') % name
    while True:
        print(content)
        operator = input('请选择(1-5):')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            delete_student()
        elif operator == '5':
            break
        else:
            print('输入有误！')
