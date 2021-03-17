# -*- coding: utf-8 -*-
# @Time : 2021/3/17 11:05
# @Author : ls
# @File : 02回合制游戏.py

"""
1、实现一个回合制格斗游戏
    函数
    循环/判断
    三木运算
    类型提示
    列表推导式

2、游戏解读
    ①一个回合制游戏，每个角色都有Hp和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200
    ②定义一个fight方法：
    my_hp = hp - enemy_power
    enemy_final_hp = enemy_hp - my_power
    两个hp进行对比，血量剩余多的人获胜
"""
# 定义个函数
def fight():
    # 定义四个变量，存放你和我的 血量和攻击力
    my_hp = 1000
    my_power = 200
    you_hp = 1000
    you_power = 199

    # 一轮对打后，我的血量和你的血量
    my_final_hp = my_hp - you_power
    you_final_hp = you_hp - my_power

    if my_final_hp > you_final_hp:
        print("哈哈，我赢了！")
    elif:
        print("你输了！")
    else:
        print("平局")

# 调用函数
fight()