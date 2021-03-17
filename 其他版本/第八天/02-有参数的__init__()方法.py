# 创建老师 name age （不同的）

# 为了创建老师类准备的
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

zhanglaoshi = Person('张老师', 40)
print(zhanglaoshi.name, zhanglaoshi.age)

# 还需要创建学生（学生有学号）
class Student(Person):

    def __init__(self, name, age, no):
        # 子类重写了父类同名方法，然后，调用父类同名方法
        # 01 父类名.方法名（）
        Person.__init__(self, name, age)
        # 02 super(子类名，self).方法名（）
        super(Student, self).__init__(name, age)
        # 03 super().方法名（） 这是方法是02的简写
        # 02 和 03 注意点：适用于单继承 或者是多继承，调用第一个父类的方法（必须是新式类）
        super().__init__(name, age)
        # 自定义
        self.no = no

    def set_info(self):
        pass

xm = Student('小明', 22, '100')
print(xm.name, xm.age, xm.no)