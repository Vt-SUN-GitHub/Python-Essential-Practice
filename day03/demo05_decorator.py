#装饰器 AOP 面向切面编程
#性能统计

#内部函数

def outerFun(a,b):
    c = a + b
    def innerFun(x,y):
        return x + y
    return  innerFun(c,a)


print(outerFun(23,32))

#闭包
def outFunc():
    a = 1
    def inFunc(x, y):
        return a + x + y
    return inFunc

f = outFunc()
r = f(12,23)
print(f.__closure__[0].cell_contents)
print(r)

import time
#装饰
def performance(f):
    def innerFunc(*args, **kw):
        start = time.perf_counter()
        result =  f(*args, **kw)
        end = time.perf_counter()
        print("执行时间为：",end-start)
        return result
    return innerFunc

#侵入式编程
def log():
    start = time.perf_counter()
    print("日志")
    end = time.perf_counter()
    print("执行时间为：" ,end-start)
    ...
log()


@performance
def printMes():
    print(1)
    print(2)
    ...
printMes()

@performance
def cal(x,y):
    print('---------')
    z = x * 10000 + y * 10000
    return z
print(cal(1000,2000))












