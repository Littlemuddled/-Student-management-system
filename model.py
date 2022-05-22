class Teacher(object):
    def __init__(self, name, password):
        import tools
        self.name = name
        self.password = tools.encrypt_password(password)  # 密码加密


class Student(object):
    def __init__(self, name, age, gender, tel):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel

