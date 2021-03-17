# # 写一个函数打印一条横线
# def print_one_line():
#     print("--" * 10)
#
# # 调用函数
# print_one_line()
#
# # 打印自定义行数的横线
# def print_lines(num):
#     # for循环
#     for i in range(num):
#         print_one_line()
#
# # 最终执行函数
# print_lines(12)

# 写一个函数求三个数的和
def add3sum(a, b, c):
    print("三个数的和等于：%d" % int(a + b + c))
    # return a + b + c  # 也可以实现单函数的返回值
    print("三个数的平均为：%d" % int((a + b + c)/3))
    # return (a + b + c)/3 # 也可以实现单函数的返回值

# add3sum(1, 3, 5)

# 函数的调用 -> 位置参数调用函数
# 使用位置参数调用函数 需要注意实参的位置
# 实参的位置和形参的位置要一一对应
# TypeError: my_func1() missing 1 required positional argument: 'b'
# 如果实参传入的少一个实参 会报错
add3sum(12, 23)
