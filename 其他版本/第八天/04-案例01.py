'''
定义一个学生类，有下面的对象属性
    姓名
    年龄
    成绩（语文，数学，英语）[每科成绩的类型为整数]
对象方法：
    获取学生的姓名：get_name() 返回类型：str
    获取学生的年龄：get_age()  返回类型：int
    返回3门科目中最高的分数，get_course() 返回类型：int
写好类以后，可以定义2个同学测试下；

'''
class Student(object):

    def __init__(self, name, age, course_list):
        # 姓名
        self.__name = name
        # 年龄
        self.__age = age
        # 成绩
        self.__course_list = course_list

    # 获取学生的姓名
    def __get_name(self):
        return self.__name
    # 获取学生的年龄
    def __get_age(self):
        return self.__age
    # 获取学生的成绩：返回3门科目中最高的分数
    def __get_course(self):
        return max(self.__course_list)

    def print_info(self):
        # print(self.__get_name(), self.__get_age(), self.__get_course())
        return self.__get_name(), self.__get_age(), self.__get_course()

xm = Student('小明', 22, [56, 67, 98])
# # 获取名字、年龄、成绩（3选1最高分）
# xm_name = xm.get_name()
# xm_age = xm.get_age()
# xm_score = xm.get_course()

# 拆包技术
xm_name, xm_age, xm_score = xm.print_info()
print(xm_name, xm_age, xm_score)