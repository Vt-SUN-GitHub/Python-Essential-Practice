'''
实战任务1. 游戏人生
业务需求：
    创建一个游戏场景，涉及3个场景和1个功能。
    场景1：草场作战，消耗战斗力200
    场景2：修炼，增长战斗力100
    场景3：多人团战，消耗战斗力500
    功能1：显示玩家状态
    当玩家战斗力为0时，阵亡！
技术需求：
    使用面向对象的封装特性实现任务的创建及场景功能的调用。
'''
import sys
import os
import random as rd
class Role:

    def __init__(self, name, sex, fighting):
        self.name = name
        self.sex = sex
        self.fighting = fighting
        ...
    def grassland(self):
        '草场作战，消耗战斗力200'
        if self.fighting < 200:
            print('[%s]: 参与草场作战失败，战斗力不足' %self.name)
            ...
        else:
            print("[%s]: 参加草场作战，消耗战斗力200" %(self.name))
            self.fighting -= 200
        if self.fighting <= 0 :
            print("[%s]: 强行参与草场作战，玩家阵亡" %(self.name))
            sys.exit()
        else:
            print("[%s]: 草场作战结束，剩余战斗力 [%d]" %(self.name,self.fighting))
            ...

    def Practice(self):
       '修炼，增长战斗力100'
       print("[%s]: 闭关修炼，增长战斗力100" %self.name)
       self.fighting += 100
       print("[%s]: 闭关结束，剩余战斗力: [%d]" %(self.name,self.fighting))
       ...

    def teamFight(self):
       '多人团战，消耗战斗力500'
       if self.fighting < 500:
           print("[%s]: 参与多人团战失败，战斗力不足" %self.name)
           ...
       else:
           print("[%s]: 参与多人团战，消耗战斗力500" %self.name)
           self.fighting -= 500
           ...
       if self.fighting <= 0:
           print('[%s]: 强行参与多人团战，玩家阵亡' %self.name)
           sys.exit()
       else:
           print('[%s]: 多人团战结束，剩余战斗力 [%d]' %(self.name,self.fighting))
           ...
       ...

    def Detail(self):
        '显示个人状态数值'
        print("--------[%s]--------" %self.name)
        print("姓名: %s" %self.name)
        print("性别: %s" %self.sex)
        print("战斗力: %d" %self.fighting)
        print('-'*20)
        ...
    ...

if __name__ == '__main__':
    os.system('cls')
    print('#'*30)
    print('任务创建')
    print('-'*30)
    role = Role('徐','女',1000)
    role.Detail()
    print('#'*30)
    print('[%s]重出江湖' %role.name)
    print('#'*30)
    while True:
        i = rd.randint(1,3)
        if i == 1:
            role.Practice()
            ...
        elif i == 2:
            role.grassland()
            ...
        else:
            role.teamFight()
            ...
        ...






