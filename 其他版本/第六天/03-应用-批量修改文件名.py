import os

# 准备工作
# 01.当前目录下创建一个文件夹
# os.mkdir("批量修改文件名文件夹")
#
# # 02.指定默认目录
# os.chdir("批量修改文件名文件夹")
# print(os.getcwd())
#
# # 03.在黑马文件夹下创建10个文件
# for i in range(1, 11):
#     # 打开文件
#     f = open('hm%d.txt' % i, 'w')
#     # 关闭文件
#     f.close()

# 实际工作
# hm.txt  -> hmx[中国].txt

# 01.指定默认目录
os.chdir("批量修改文件名文件夹")
ret = os.getcwd()
print(ret)

# 02.获取当前目录下的目录列表
my_list = os.listdir()

# 03.遍历my_list
for file_name in my_list:
    # 得到新的文件名
    new_file_name = file_name.replace(".txt", ".[中国]txt")
    # 对文件重命名
    os.rename(file_name, new_file_name)
print(os.listdir())