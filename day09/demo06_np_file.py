import numpy as np

array1d = np.array([1,2,3,4])

array2d = np.array([[2,3,4,5],
                    [6,7,8,9]])

np.savez('a.npz', array1d=array1d, array2d=array2d)

dc = np.load('a.npz')
print(dc['array1d'])
print(dc['array2d'])
