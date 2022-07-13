#lambda表达式
lambdaSum = lambda x,y:x+y

print(lambdaSum(1,2))

#三元表达式
x = 20
y = 10
print(x if x>y else y)

#推导式
data = []
for i in range(1,100):
    data.append(i**2)
    ...
print(data)

data1 =[i**2 for i in range(1,100)]
print(data1)

fun = lambda x, *args,  y=10, **kwargs: x+y+sum(args)+kwargs['age']

print(fun(10,10,10,age=1))

#if elif else while for 不构成作用域范围
i = 0

if i >= 0 :
    j = 2
    pass

print(j)

#递归 需要消耗栈内存，栈有限
def fab(n):
    if n ==1:
        return n
    else:
        return n*fab(n-1)

print(fab(5))
# print(fab(999)) RecursionError: maximum recursion depth exceeded in comparison

