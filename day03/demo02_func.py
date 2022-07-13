#函数

def sum(x,y):
    return x+y

print(sum(1,2))

def printInfo(name, age, moeny):
    print("name: %s, age: %d, money: %.2f" %(name,age,moeny))
    return None

printInfo("zhangSan",21,21.21)

#传值还是传引用
info = {'hobby':['篮球']}
print(info['hobby'])

