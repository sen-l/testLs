'''
try:
    执行可能发生异常的代码01（不同的异常类型）
    执行可能发生异常的代码02（不同的异常类型）
except (异常类型1， 异常类型2，...):
    如果发生异常执行的代码
'''
# print(num)  # NameError: name 'num' is not defined

try:
    # 可能有异常
    open('h2m.txt', 'r')
except (FileNotFoundError, NameError):
    print('捕获到异常了~~~')