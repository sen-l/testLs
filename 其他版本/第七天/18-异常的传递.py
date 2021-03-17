# try嵌套

# try:
#     try:
#         open('hm8.txt', 'r')
#     finally:
#         print('里面的finally！')
# except:
#     print('捕获到了异常了！')

# 第一种
# def my_func1():
#     print(num)
# def my_func2():
#     my_func1()
#
# def my_func3():
#     my_func2()
#
# try:
#     my_func3()
# except:
#     print('异常')


# 第二种
# def my_func1():
#     print(nnn)
#
# def my_func2():
#     my_func1()
#
# def my_func3():
#     try:
#         my_func2()
#     except:
#         print('异常第二种')
# my_func3()

# 第三种
# def my_func1():
#     print(num)
#
# def my_func2():
#     try:
#         my_func1()
#     except:
#         print('异常')
#
# def my_func3():
#     my_func2()
#
# my_func3()

# 正确方式
def my_func1():
    try:
        print(mmm)
    except:
        print("正确的捕获异常方式")

def my_func2():
    my_func1()

def my_func3():
    my_func2()

my_func3()

# 捕获异常是可以传递的