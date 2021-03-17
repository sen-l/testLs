# 自定义两个类
class Person1(object):

    def __init__(self, age):
        self.age = age

    def AAA(self):
        print('AAA')

    def BBB(self):
        print('bbb')

class Person2(object):


    def __init__(self, no):
        self.no = no

    def BBB(self):
        print('BBB')

# 自定义一个类 名字，年龄，学号 AAA BBB CCC DDD
class Student(Person1, Person2):
    # # 子类重写父类的同名方法
    # 为什么要重写，做自己特有的事情 -》 self.name = name
    def __init__(self, name, age, no):
        # 自定义
        self.name = name
        # 继承过来
        Person1.__init__(self, age)
        Person2.__init__(self, no)

    # 继承了父类的Person1 AAA
    # 继承了父类Person2 CCC
    # 重写BBB方法，子类调用同名方法完成
    def BBB(self):
        Person1.BBB(self)
        # Person2.BBB(self)
        # print('hhh')

    def CCC(self):
        print('CCC')

    def DDD(self):
        print('DDD')

xg = Student('小刚', 22, '122')
print(xg.name, xg.age, xg.no)
xg.AAA()
xg.BBB()
# 单独开辟内存，不建议
Person2('120').BBB()
xg.CCC()
xg.DDD()