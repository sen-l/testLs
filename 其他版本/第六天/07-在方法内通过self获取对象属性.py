# 自定义一个犬类来创建各种叫名字旺财的狗，年龄：5，皮色：黑色，会吃骨头

# 自定义一个类
class Dog(object):
    # 方法
    def eat(self):
        print("狗狗吃骨头")

    # 自定义一个方法，完成打印对象的属性
    def info(self):
        print(self.name, self.age, self.color)

# 自定义一个旺财对象
wangcai = Dog()
# 对象方法
wangcai.eat()
# 给对象添加属性：名字
wangcai.name = "旺财"
# 年龄
wangcai.age = 4
# 颜色
wangcai.color = '黑色'
# 使用对象名调用对象方法
wangcai.info()
# 在类的外面，使用的是对面名.属性名
# 在类的实例方法内部，使用的是self.属性名（self == 调用这个对象方法的对象）