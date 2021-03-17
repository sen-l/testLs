# encoding:utf-8

# 统计字符串中，各个字符的个数
# <1>准备一个字符串
my_str = "hello world"
# 字符串有一个count
# 循环-> for 循环
# 定义一个列表
my_list = []
# 循环
for c in my_str:
    # 去处空格，且这个字符列表没有保存过
    if c != " " and c not in my_list:
        # 计算每个字符出现的次数
        count = my_str.count(c)
        print("%s:%d" % (c, count))
        # 保存下这个字符
        my_list.append(c)


# <2>准备一个字符串
my_str = "hello world"
# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
new_list = my_str.split()
print(new_list)
new_str = "".join(new_list)
print(new_str)
# 字符串的有一个count
# 循环->for 循环
# 定义一个列表
my_list = []

for c in new_str:
    # 这个字符列表没有保存过
    if c not in my_list:
        # 计算每个字符出现的次数
        count = my_str.count(c)
        print("%s:%d" % (c, count))
        # 保存下这个字符
        my_list.append(c)


