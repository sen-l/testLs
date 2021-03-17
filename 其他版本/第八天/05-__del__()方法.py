class Hero(object):
    # 监听对象创建成功，会执行Init方法
    def __init__(self):
        print('__init__')

    # 追踪对象属性值变量
    def __str__(self):
        return '__str__'

    # 监听对象销毁后，会执行del方法
    # 待对象的引用技术为0的时候才会执行
    def __del__(self):
        print('888888')

swk = Hero()

sek1 = swk
sek2 = sek1
del swk
del sek1
del sek2
input()