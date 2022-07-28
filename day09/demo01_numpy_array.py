import numpy as np

array1 = np.array([1,2,3,4,5])
array2 = np.array([5,6,7,8,9])

print(array2 + array1)
print(array2 - array1)
print(array2 * array1) # 元素相乘

array2D = np.array([[1,2,3,4],[5,6,7,8]])
print(array2D)
print(array2D ** 2)
print(np.sqrt(array2D)) #开方

#n*m*k
array3D =np.array([[[1,2,3,4],[2,3,4,5]],[[3,4,5,6],[4,5,6,7]]], dtype=np.int32)
print(array3D.dtype) #数字类型
print(array3D.shape) #查看维数

arr = np.array([[1,2,3],
               [4,5,6]])
arr1 = np.array([[2],
                 [3],
                 [4]])

print(arr.dot(arr1)) #矩阵相乘
print(arr @ arr1)

array = np.arange(0,20).reshape(2,2,5) # n*m*k = j-i
print(array)