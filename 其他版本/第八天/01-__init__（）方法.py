# class Person(object):
#     # 构造方法：已两个下划线开头，再以两个下划线结尾的方法
#     # 在特殊的情况下，被python调用（程序员也可以手动调用）
#     def __init__(self):
#         self.name = '小明'
#         self.age = 20
#
# xx = Person()
# xx.name, xx.age
#
# yy = Person()
# yy.name, yy.age
'''
xx 和 yy 这两个对象的地址肯定不同，需要分别开辟内存空间保存

xx.name, xx.age
yy.name, yy.age

python中提供了一个小整数缓存池（-5~256）直接，减少内存的浪费，提供程序的性能
字符串、元组、字典、列表，也有缓存池，小于2kb（了解）

'''

class Person(object):

    def __init__(self):
        self.name = '小明'
        self.age = 20
# 继承Person类
class Strudent(Person):
    pass

xm = Strudent()
print(xm.name, xm.age)