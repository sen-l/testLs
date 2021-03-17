# 假设 len函数
# 函数的文档说明 --> 加的文档说明  是python
help(len)
# len python内置函数 python创建

# 很多的时候需要程序员自己创建
# 自定义一个函数
def add2num(num1, num2):
    return num1 + num2

# 如果一个自定义函数，没有文档说明，默认是用help会打印函数上面的注释
help(add2num)

# 自定义一个函数
def add3num(num1, num2):
    # 单行注释：下面是文档说明
    """
    这个函数是用来计算两个数的和的
    :param num1: 参数1
    :param num2: 参数2
    :return: 返回值是两个数字相加
    """
    return num1 + num2

help(add3num)