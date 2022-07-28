import numpy as np

#数组的数据类型
arr = np.array([1,2,3,4,5],dtype=float) #和电脑的操作系统有关系（float64）
print(arr)

strArr = arr.astype(dtype=np.str_)
print(strArr)

intArr = arr.astype(np.int64)
print(intArr)

boolArr = np.array([True, False, True, False], dtype=bool)
print(boolArr)

print(boolArr.astype(np.int64))

print(boolArr.astype(np.str_))

#矢量化计算
print(arr+1)

print(1/arr)

