import numpy as np
from  day10.funcLibrary import line


#自然对数
print(np.exp(1))
line()

#sigmoid激活函数
def sigmoid(x):
    return 1/(1+np.exp(-x))

print(sigmoid(0))
line()

#数组运算
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print(np.add(arr1,arr2))
print(np.subtract(arr2,arr1))
line()

#次方运算
print(np.power(2,10))
print(2**10)
line()

#返回一个浮点数组的小数部分和整数部分
farray = np.array([1.1,2.222,3.3333,4.44444])
print(np.modf(farray))
line()

#对数函数
print(np.log(np.e))
line()

#np.where
arr3 = np.arange(1,21)
print(np.where(arr3 % 2 ==0, arr3, -1))
line()

#嵌套np.where (成绩分类)
scores = np.random.randint(0,100,size=(100))
print(np.where(scores >= 90, ':优秀', np.where(scores >= 70, ':良好', ':一般')))
line()

boolArr = (scores >= 60)
print(boolArr.all())
print(boolArr.any())
line()

#排序函数在源数据上操作
print(np.sort(scores))
line()

#unique 返回唯一值，和排序后的结果
print(np.unique(scores))


