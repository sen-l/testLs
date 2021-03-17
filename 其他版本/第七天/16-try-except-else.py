try:
    open('hm.txt', 'r')
except Exception as e:
    print(e)
else:
    # 如果try中的代码没有发生异常，就会执行else中的代码
    print('else')