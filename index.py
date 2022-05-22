import file_manager

import model
import student_manager


def login():
    data = file_manager.read_json('data.json', {})  # 读取文件数据
    teacher_name = input('请输入老师账号:')
    if teacher_name not in data:
        print('登录失败！该账号没有注册！')
        return
    password = input('请输入密码:')
    import tools
    if data[teacher_name] == tools.encrypt_password(password):
        student_manager.name = teacher_name  # 老师
        student_manager.show_manager()  # 调用学生管理页面并对学生进行操作
    else:
        print('密码错误！登录失败！')



def register():
    # 读取文件查看文件里面有没有数数据，如果文件不存在，默认是一个字典
    data = file_manager.read_json('data.json', {})
    while True:
        teacher_name = input('请输入账号(3-6位):')
        if 3 > len(teacher_name) > 6:
            print('账号不符合要求，请重新输入！')
        else:
            break
    if teacher_name in data:
        print('注册失败！该账号已经被注册过！')
        return

    while True:
        password = input('请输入密码(6-12位):')
        if 6 > len(password) > 12:
            print('密码不符合要求，请重新输入！')
        else:
            break
    t = model.Teacher(teacher_name, password)
    data[t.name] = t.password
    # data[teacher_name] = password  # 将账号和密码加到字典里面
    file_manager.write_json('data.json', data)


def start():
    # file_manager.base_dir = './XXX/'
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '\n请选择(1-3):')
        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            break
        else:
            print('输入有误')


if __name__ == '__main__':
    start()
