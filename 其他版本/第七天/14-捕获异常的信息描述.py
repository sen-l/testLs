'''
try:
    执行可能发生异常的代码
excpet 异常类型 as 临时变量名：
    可以获得临时变量名
'''
# try:
#     open('hm3.txt', 'r')
# except FileNotFoundError as e:
#     # as 临时变量，使用临时变量保存异常的信息描述
#     print('捕获到异常了！', e)


"""
try:
    执行可能发生异常的代码
excpet (异常类型1, 异常类型2, ....) as 临时变量名:
    可以获得临时变量名
"""

try:
    open('hm4.txt', 'r')
    print(bb)
except (FileNotFoundError, NameError) as e:
    print(e)