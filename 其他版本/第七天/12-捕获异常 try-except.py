'''
try:
    执行可能发生异常的代码
except 异常类型：
    如果发生异常执行的代码
'''

try:
    open('hm1.txt', 'r')
    print('测试')
    print(num)
except FileNotFoundError:
    print('文件没找到异常')
    open('hm.txt', 'w')

print('继续运行')