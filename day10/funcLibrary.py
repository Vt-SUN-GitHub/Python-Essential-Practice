import random as rd

def line():
    print('-------------')
    ...

#随机获取颜色
def randomColor():
    colorArr =['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color  =''
    for i in range(6):
        color += colorArr[rd.randint(0,14)]
        ...
    return '#'+color