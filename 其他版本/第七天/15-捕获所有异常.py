# 获取所有异常的信息描述
'''
try :
    执行可能发生异常的代码
except Exception as 临时变量:
    发生异常执行的代码
'''

try:
    open('hm5.txt', 'r')
    open(mmm)
except Exception as e:
    print('捕获异常了！', e)