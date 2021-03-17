# 定义类 -> 自定义类

# python 创建的list类
# class list(object):

# 开发 王者荣耀  我想创建一个悟空（对象） -> 类（英雄类） -> 类型（Hero）

# 自定义类
# class 标识这一个类

# 快速查看某个类的源文件实现，点击类名 Ctrl + 鼠标左键

# 三种类的创建方式都是在python2.x产生的
# object 是所有类的父类
# 03 是后期产生的
# 01 02 叫做经典类，他们都是没有父类（基类）的
# 03 叫做新式类

# python3.x中，无论写01 02 03 哪种方式都是继承于object类
# 但是如果在python2.x中他是区分 01 02 相同，而03 是有父类的

# 01
class Hero:
    pass

# 02
class Hero():
    pass

# 03 建议这么写
class Hero(object):
    pass
