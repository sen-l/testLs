# -*- coding: utf-8 -*-
# @Time : 2021/3/17 16:50
# @Author : ls
# @File : 03类与对象、类继承.py

class Bike:


    def run(self,km):
        print(f"骑行了{km}km")

class Ebike(Bike):
    # 类属性 valume 电量
    def __init__(self,valume2):
        self.valume = valume2
    # 用来充电，vol为电量
    def fill_change(self,vol):
        print(f"已充电{vol}度")
        print(f"充电之后还有{vol +self.valume}度")
        self.valume = vol + self.valume

    def run(self,km):
        # 电量能跑的公里数
        e_km = self.valume*10
        print("电量能跑的最远公里数：",e_km)

        if e_km >= km:
            print(f"用电跑了{km}km")
        else:
            print(f"用电跑了{e_km}km")
            # print(f"用力跑了{km - e_km}km")
            # 调用父类方法
            super().run(km - e_km)



# 实例化有初始化属性的类时，需要传属性的值
my_bike = Ebike(100)
my_bike.fill_change(10)
my_bike.run(10000)