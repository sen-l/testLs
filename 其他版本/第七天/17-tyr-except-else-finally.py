try:
    open('hm.txt', 'r')
except Exception as e:
    # try中的代码发生了异常执行excepy代码
    print(e)
else:
    # try中的代码没有发生异常，就会执行else代码
    print('else')
finally:
    # 无论try中的代码是否发生异常，finally都会执行
    print('finally11111')

try:
    open('hm7.txt', 'r')
except:
    print('excepy222')
finally:
    print('finally222')

# 根本就没有捕获异常，还是会发生异常的（程序崩溃）
try:
    open('hm8.txt', 'r')
finally:
    print('finally333')
# FileNotFoundError: [Errno 2] No such file or directory: 'hm8.txt'