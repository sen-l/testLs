# encoding:utf-8
# 列表是可变的
# 元组是不可变的

# 定义一个字符串 "" 或者 ''
# 定义一个列表 []
# 定义一个元组 ()

# 定义一个元组
my_tuple = (1, 3.14, True, "HELLO")
# 查看数据类型<class 'tuple'>
print("数据类型是：", type(my_tuple))

# 定义一个空元组(两个都是空元组)
my_tuple2 = ()
print(type(my_tuple2))
my_tuple3 = tuple()
print(type(my_tuple3))

# 特例
# 如果元组中只有一个元素
# 人为的把一个整数用小括号包裹起来，还是认识int类型
# （1，） -> 元组 （1） -> int
my_tuple4 = (1,)
print(type(my_tuple4))

# 通过下标获取元组中的元素
my_tuple5 = (1, 3.14, True, 3.14,"HELLO")
print(my_tuple5[3])

# 通过下标修改元组的元素
# my_tuple5[3] = 666 # 会报错IndentationError: unexpected indent
# 因为元组是不可变的，不可以修改元素 或者删除元素
# 只能查看元素 或者遍历元组中的元素

# 元组中元素的位置 index
print(my_tuple5.index(3.14))

# 元组中元素的出现的次数 count
print(my_tuple5.count(3.14))

# for 循环遍历
for value in my_tuple5:
    print(value)

# while 循环遍历
index = 0
while index < len(my_tuple5):
    print("while 循环遍历：", my_tuple5[index])
    index += 1


# 元组是不可变的  列表是可变的?
# 有时候我们需要保存一些数据 而这些数据不会改变 那么久应该使用元组进行保存
# 元组的不可变 是为了数据安全考虑
# my_tuple = ("hello", 3.14)
# my_tuple[0]
# my_tuple[1] = 3.1415926