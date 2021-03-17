# 自定义一个人类
class Person(object):

    # 监听python使用其类创建对象，并返回对象 -》 __init__
    def __new__(cls, *args, **kwargs):
        print('__new__')
        s = object.__new__(cls)
        print(s)
        return s

    # 构造方法（监听python使用其类创建对象完成，给这个对象设置属性）
    def __init__(self):
        print('__int__')
        print(self)
        self.name = '小明'

    # # 监听对象属性信息变化
    # def __str__(self):
    #     return "名字：%s" % self.name

    # 监听对象销毁的
    def __del__(self):
        print('bye bye!!!!!!!!!!')

# 创建一个对象
xiaoming = Person()
print(xiaoming)

# None 空值类型
# <class 'NoneTyep'> -> NULL  nil 没有值的意思
print('3333333333333')
print(type(None))