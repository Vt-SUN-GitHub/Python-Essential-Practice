#编写猜拳游戏(第一天作业）
import random as rd
import time

game = ['剪刀','石头','布']

def printMes(x,user,computer):
    if x == 1:
        print("你输了")
        print("电脑出" + game[computer] + ", 你出的" + game[user] +" "+game[computer]+">"+game[user])
    elif x == 0:
        print("你赢了")
        print("电脑出" + game[computer] + ", 你出的" + game[user] +" "+game[user]+">"+game[computer])
    ...


print("---游戏开始： Loading效果---")
print("Loading", end="")

for i in range(18):
    print(".",end= '',flush=True)
    time.sleep(0.2)
print()

print("1、开始游戏   2、结束游戏")
option = input("请选择:>")

if option == "1":
    print("游戏中输入exit即可退出")
    while True:
        user = input("请输入您的选项： 1:剪刀，2:石头，3:布:>")
        computer = str((rd.randint(1,3)))
        if user == computer:
            print("平局")
            ...
        elif (user == "1" and computer == "2") or (user == "2" and computer == "3") or (user == "3" and computer == "1"):
            printMes(1,int(user)-1,int(computer)-1)
            ...
        elif (user == "1" and computer == "3") or (user == "2" and computer == "1") or (user == "3" and computer == "2"):
            printMes(0,int(user)-1,int(computer)-1)
            ...
        elif user == "exit":
            break
        else:
            print("请按照游戏规则进行输入（exit即可退出游戏）")
            ...
    ...
else:
    ...
