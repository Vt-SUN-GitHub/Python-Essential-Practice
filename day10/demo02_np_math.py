import numpy as np
from day10.funcLibrary import line

array =np.arange(1,21).reshape(4,5)
print(np.sum(array))
line()

print(array)
line()

#轴
print(np.sum(array, axis=0))
print(np.sum(array, axis=1))
line()

print(np.mean(array))
print(np.mean(array, axis=1))
line()

#argmax 返回相应维度axis上的最大值的位置
arr = np.array([0.1,0.01,0.001,0.00001])
print(np.argmax(arr))
line()

#True的个数总和
print((array % 2 == 0).sum())
print(arr.sum(axis=0))
line()


