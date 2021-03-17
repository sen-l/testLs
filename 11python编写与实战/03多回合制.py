# -*- coding: utf-8 -*-
# @Time : 2021/3/17 11:19
# @Author : ls
# @File : 03多回合制.py
"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
# 定义个函数
def fight():
    # 定义四个变量，存放你和我的 血量和攻击力
    my_hp = 1100
    my_power = 100
    you_hp = 1000
    you_power = 100

    # 对打多轮，谁的血量先小于等于0，谁就输了
    while True:
        my_hp = my_hp - you_power
        you_hp = you_hp - my_power
        print("我的血量",my_hp)

        if my_hp<=0:
            print("我剩余血量为",my_hp)
            print("你剩余血量为",you_hp)
            print("我shu了！")
            break

        elif you_hp<=0:
            print("我剩余血量为", my_hp)
            print("你剩余血量为", you_hp)
            print("你输了！")
            break


# 调用函数
fight()