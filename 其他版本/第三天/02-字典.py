# encoding:utf-8

# 字典是无序的，可变的

# 定义一个字典：名称、年龄、学号
my_dict = {"name": "小红", "age": 22, "no": 1001}

# <1>修改元素
# 字典的每个元素中数据是可以修改的，只要通过key找到，即可修改
# 通过key 获取对应key的value的值
print(my_dict["name"])

# <2>添加元素
# title - "哈哈"
# 格式：字典名[key] = value
# 如果使用上面的格式，如果这个key不存在，添加一组键值对
# 如果使用上面的格式，如果这个key存在，会把key原来的value的值进行覆盖
my_dict["name"] = "小明"
print(my_dict["name"])

# <3>删除元素
# del （python内置函数） 删除键值对 格式: del 字典名[key]
# clear() 删除字典中的所有的元素
del my_dict["no"]
print(my_dict)

my_dict.clear()
print(my_dict)

# 定义一个字典
my_dict2 = {"name": "小军", "age": 22, "no": "009"}

# <4>len() 测量字典中，键值对的个数
print(len(my_dict2))

# <5>keys 返回一个包含字典所有key的列表
print(my_dict2.keys())

# <6>values 返回一个包含字典所有value的列表
print(my_dict2.values())

# <7>items -> 最外层是一个列表，每个元素是一个元组 [元素1(key, value), 元素2（key, value）]
print("====", my_dict2.items())
# 获取no ['no', '009']
my_list = my_dict2.items()
print(list(my_dict2.items())[2])
#print(my_list[2]) # 会报错，原因参考下面
'''
错误代码为：movieTitle.items()[:5]

错误原因：在Python 2.X中, movieTitle.items()返回的是一个 list, 但是在Python 3.X
中返回的是一个dict_keys object；

修改方式：list(movieTitle.items())[:5]]
'''

