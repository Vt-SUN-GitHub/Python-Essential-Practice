def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def cal(x,y,f):
    return x*y + f(x,y)

print(cal(12,23,sum))
print(cal(12,23,sub))

print(list(map(lambda x :x**2 , [1,2,3,4,5])))

print(list(filter(lambda x : True if x%2 ==0 else False, [1,2,3,4,5,6])))
