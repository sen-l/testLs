# 自定义一个人类
class Person(object):

    def __init__(self):
        self.name = "小明"
        self.age = 20

    def eat(self):
        print("肯德基")
        print("="*20)

# 自定义一个犬类
class Dog(object):

    def __init__(self):
        self.name = "旺财"
        self.age = 2

    def eat(self):
        print("吃骨头")
        print("="*25)

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

xiaoming = Person()
print(xiaoming.name)
print(xiaoming.age)
xiaoming.eat()

xiaohong = Person()
xiaohong.name = '小红'
print(xiaohong.name)
print(xiaohong.age)
xiaohong.eat()

# 函数（object为使用Person创建出来的对象服务的）
def my_print(object):
    # python中不关心函数（方法）中参数的类型，只要这个参数这个属性或者这个方法，就可以使用
    print(object.name)
    print(object.age)
    object.eat()
my_print(xiaoming)
my_print(xiaohong)

# 狗对象
wangcai = Dog()
my_print(wangcai)

# 多态的好处？
# 给函数或者方法，增加的扩展性和提高开发效率