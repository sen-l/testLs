# 如果一个模块中使用了 __all__
# 只用在 __all__ 的列表中的字符串才可以在其他模块中使用
# 条件：其他模块必须通过 from 模块名 import * 方式导入模块
__all__ = ['name']

# 全局变量
name = '加法运算'

# 函数
def add2num(a, b):
    return a + b

# 类
class Person(object):

    def eat(self):
        print("人吃吃")

# git 或者是 svn -》 远程仓库
# 在自己定义一个模块中，进行自测（程序员做的事情）

# 定义一个函数 -》 自测函数
def main():
    print(name)

    ret = add2num(10, 20)
    print(ret)

    p = Person()
    p.eat()

if __name__ == '__main__':
    main()