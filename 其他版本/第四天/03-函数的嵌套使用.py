# encoding=utf-8

# 定义一个函数
def my_func1():
    print("my_func1开始")
    print("my_func1结束")

# 定义一个函数
def my_func2():
    print("my_func2开始")
    my_func1()
    print("my_func2结束")

my_func2()
