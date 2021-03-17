# 定义一个变量保存文件名
file_name = 'hm.txt'

# # <1>写数据（write）
# # 以只写模式打开文件
# f = open(file_name, 'w')
# # 写数据
# f.write("hello + world!!!")
# # 关闭文件
# f.close()

# # <>读数据（read），如果使用字符串方便
# # 以只读模式打开文件
# f = open(file_name, 'r')
# # 读取数据
# ret = f.read()
# # 打印数据
# print(ret)
# # 关闭文件
# f.close()

# # <3>读数据(readlines)，如果使用列表方便
# # 以只读模式打开文件
# f = open(file_name, 'r')
# # 读取数据
# # 把每行的数据保存到列表中
# ret = f.readlines()
# print(ret)
# # 关闭文件
# f.close()

# 如果以w方式打开文件，会把原来文件的数据清空，然后再写入
f = open(file_name, 'w')
f.write('nihao,nibuhaohao!!!')
# 关闭文件
f.close()

f = open(file_name, 'r')
ret = f.readlines()
print(ret)
# 关闭文件
f.close()

# a 追加数据
f = open(file_name, 'a')
f.write(('hhhhhhhhhhhhhhhhhhhhhh'))
# 关闭文件
f.close()

f = open(file_name, 'r')
ret = f.readlines()
print(ret)
# 关闭文件
f.close()