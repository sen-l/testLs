# 匿名函数：对函数的简写

# 无参数无返回值的函数
def my_print():
    print("hello world!!!")

my_print()

# 表达式的定义
f = lambda : print("hello  python!!!")
# 执行
f()
# 等价于
(lambda : print("hello  python!!!"))()

# 无参数有返回值的函数
def my_pi():
    return 3.14
print(my_pi())

# 表达式的定义
f = lambda : 3.14
print(f())

# 定义一个有参数无返回值的函数
def my_print2(name):
    print("你好%s" % name)

my_print2("老李头")


# 定义一个有参数有返回值的函数
def add2num(a, b):
    return a + b
print("add2num函数返回值为：%d" % add2num(3, 5))

f = lambda a, b : a + b
print("f函数返回值为：%d" % f(10, 20))

# 函数作为参数传递
# 表达式
f = lambda x, y : x + y

# 函数
def fun(a, b, opt):
    print("a = %d" % a)
    print("b = %d" % b)
    result = opt(a, b)
    print("result = %d " % result)
# 调用函数
fun(1, 2, lambda x, y : x + y)

def add3num(x, y):
    return x + y

f = lambda x, y : x + y
def fun2(a, b, opt):
    result = opt(a, b)
    print("result = %d " % result)

fun2(10, 11, f)
print("-----------------------------------------------")

# 自定义排序（最外层肯定是列表）
my_list = [1, 4, -10, 20, 3]
my_list.sort()
print(my_list)

stus = [{"name": "张三", "age": 18}, {"name": "李武", "age": 19}, {"name": "王琦", "age": 17}]
stus2 = [{"name": "zhangsan", "age": 18}, {"name": "liwu", "age": 19}, {"name": "wangqi", "age": 17}]
print("未排序之前：%s" % stus)
# 按照年龄排序
stus.sort(key=lambda my_dict:my_dict["age"])
print("按年龄排序之后：%s" % stus)

# 按照名字排序
# 使用的每个名字的首字母排序（规则是按ascii码完成的）
# 格式: 列表名.sort(key=lambda 列表的元素(临时变量): 临时变量[key])
stus2.sort(key=lambda  my_dict:my_dict["name"])
print("按名字排序之后：%s" % stus2)

# 列表中的列表嵌套
my_list = [[12, 8, 9], [7, 10, 11], [9, 10, 22]]
# 按照列表元素（小列表）最后一个元素排序
# 格式: 列表名.sort(key=lambda 列表的元素(临时变量): 临时变量[下标索引])
my_list.sort(key=lambda new_list:new_list[2], reverse=True)
print(my_list)
my_list.sort(key=lambda new_list:new_list[0], reverse=True)
print(my_list)