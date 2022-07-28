import numpy as np

array1d = np.array([1,2,3,4])
print(array1d.T)
print()

array2d = np.array([[1,2,3],[4,5,6]])
print(array2d.T)
print()

#转置即下标的转换
array3d = np.array([[[1,2,3],
                     [2,3,4]]])
print(array3d.shape)
print(array3d.T.shape)

