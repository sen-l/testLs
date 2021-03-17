class Person(object):

    def __init__(self):
        self.name = '小红'
        self.age = 22

    def __str__(self):
        return '姓名：%s，年龄：%d' % (self.name, self.age)

xh = Person()
print(xh)
xxh = Person()
print(xxh)