# encoding:utf-8
import random
# 开区间、闭区间

# 随机数
#[x, y]
#random.randint(x, y)

# 范围
# [x, y]
# "a"[x:y:步长]

# 数据类型，是可变，还是不可变
# 不可变的
# in float bool str 元组

# 可变的
# 列表 字典

# 公共方法
# 运算符 +
# 列表  注意顺序
my_list1 = [1, 2]
my_list2 = [3, 5]
ret1 = my_list1 + my_list2
print(ret1)
# 字符串
name = "熊明"
# 占位符
print("我叫%s" % name)
ret = "我叫" + name
ret1 = "我叫s%" + name
print(ret)
print(ret1)

# 类型不统一，使用str()转类型
name = "小红"
age = 18
ret2 = "我叫" + name + ",年龄" + str(age)
print(ret2)

# 元组
ret3 = (1, 4) + (3, 6)
print(ret3)

# 运算符 *
# 字符串
my_str = "=="*20
print(my_str)

# 列表
my_list = ["hello", "world!"]*10
print(my_list)

# 元组
my_tuple = (11,)*5
print(my_tuple)

# in
my_name = "world"
if "l" in my_name:
    print("存在！！！")

# 元组
my_tuple = (1, 2, 3)
if 2 in my_tuple:
    print("真的存在吗？")

# 字典
my_dict = {"name": "小红", "age": 22, "no": "009"}
# 使用in 在字典中其实判断是key存不存在
if "age" in my_dict:
    print("真真的存在·！")
if "小红" in my_dict:
    print("应该是不存在的。")

# del 用法总结
# 可以配合列表使用
my_list = [1, 2, 4, 5]
del my_list[1]
print(my_list)

# 可以配合字典使用
my_dict = {"name": "小花", "age": 22, "no": "009"}
del my_dict["no"]
print(my_dict)

# 可以提前销毁一个对象
num = 10
# 在程序么有结束的时候，程序员提前杀死了这个对象，提前释放内存
# NameError: name 'num' is not defined
# del num
# print(num)
# # 组织程序结束
# input()
# 监听当程序结束后 python会执行一个方法 del num 告知系统回收内存