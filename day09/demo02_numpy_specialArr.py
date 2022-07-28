import numpy as np

#定义特殊数组
print(np.zeros(shape=(2,2,2)))
print()
print(np.ones(shape=(3,3)))
print()
print(np.identity(5))#单位矩阵
print()
print(np.diag([1,2,3,4,5]))
print()
print(np.empty(shape=(4,5)))#一般不用
print()
array =np.arange(0,4,0.1)
print(array)