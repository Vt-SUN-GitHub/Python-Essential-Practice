import numpy as np
from day10.funcLibrary import line

#linalg函数列表

# dot  @
arr1 = np.array([[1,2,3],
                 [4,5,6]])
arr2 = np.array([[1,2],
                 [3,4],
                 [5,6]])
print(arr1.dot(arr2))
print(np.dot(arr1,arr2))
line()

#n*n
array = np.array([[1,2],
                  [3,4]])
q,v = np.linalg.eig(array)
print(q)
print(v)
line()

#逆矩阵 V.dot(V') = E
v = np.linalg.inv(array)
print(v)
print(array.dot(v))
line()

#meshgrid
point = np.arange(0,10,1)
vx, vy = np.meshgrid(point,point)
print(vx)
print(vy)

