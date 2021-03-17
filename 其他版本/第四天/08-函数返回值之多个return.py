# 定义一个函数，当执行函数的时候，传入一个分数，可以返回一个字符串（优 良 中 差）
# 包含多个return
def my_func(score):
    # 对分数进行判断
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "中"
    elif score >= 0:
        return "差"
    print("测试测试") # 它不会执行，因为最后一个return已经执行了

ret = my_func(89)
print(ret)

def my_func1():
    print("开始")
    # 只要函数中执行了return，提前结束函数的执行，而且return后面的代码将不再执行
    return "3.14"
    print("开始111")
    return 20
    print("结束")

print(my_func1())


# return 的总结

# 01-作为函数的返回值
# 02-执行的函数提前结束 (为了提高性能考虑)