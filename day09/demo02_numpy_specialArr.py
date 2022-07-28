import numpy as np

#定义特殊数组
print(np.zeros(shape=(2,2,2))) #零矩阵
print()

print(np.ones(shape=(3,3))) #所有元素为1的矩阵
print()

print(np.identity(5))#单位矩阵
print()

print(np.diag([1,2,3,4,5])) #对角线元素为指定的单位矩阵
print()

print(np.empty(shape=(4,5)))#一般不用 （输出为空数组）
print()

array =np.arange(0,4,0.1) #按0.1分割0-4 生成带起点和终点的特定步长的排列。
print(array)
print()

array = np.arange(1,21).reshape((4,5))
print(array)
print(np.ones_like(array))
print()

print(np.eye(4,5))

