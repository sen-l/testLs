# encoding:utf-8
# 定义一个字典
my_dict2 = {"name": "小军", "age": 22, "no": "009"}

# 遍历- key
for key in my_dict2.keys():
    print(key)

# 遍历- value
for value in my_dict2.values():
    print(value)

# 遍历- items
for item in my_dict2.items():
    print(item)

# 通过设置两个临时变量
for key, value in my_dict2.items():
    print("key:", key)
    print("value:", value)

# 如果想使用元素和下标索引，请使用enumerate(列表名)
# 定义一个列表
my_list = list("abcdef")
# 不就要获取列表中的元素，而且需要知道这个元素下标索引
for i, value in enumerate(my_list):
    print(i, value)