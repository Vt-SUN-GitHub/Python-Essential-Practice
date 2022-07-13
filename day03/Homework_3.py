#课堂作业，自己编写实现range的功能，支持小数步长
def myRange(x, y, z):
    while True:
        if(x > y):
            break
        yield x
        x += z
        ...


for i in myRange(0, 2, 0.1):
    print(i,end=" ")
    ...
print()

'''
使用装饰器是实现统一日志打印，在每次调用某个函数的时候，
都要输出函数调用的函数名称，调用的时间（年月日时分秒）。
'''
import datetime
import time
from functools import wraps

def callLog(f):
    @wraps(f)
    def innerFunc(*args, **kw):
        callTime = datetime.datetime.now()
        print("调用时间为: ",callTime)
        print("函数调用的函数名称: ", f.__name__)
        return f(*args, **kw)
    return innerFunc

@callLog
def sub(x, y):
    return x - y

@callLog
def sum(x, y):
    return x + y

def printMes():
    print(sub(12,23))
    time.sleep(0.1)
    print(sum(12,23))

printMes()

