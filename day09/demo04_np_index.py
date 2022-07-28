import numpy as np

#索引即下标
arr = np.array([[1,2,3],[4,5,6]])
print(arr[0][0])

arr1 = np.arange(1,21).reshape(2,2,5)
print(arr1[0])#正着找
print(arr1[-1])#负着找
print()

#start, stop, step
print(arr1[:,-1,:])
print()

#切片是在arr的地址上修改数值
arr1[-1,-1,-1] = 1
print(arr1)
print()

chips = arr1[:,-1,-1]
print(chips)
print()

chips2 = arr1[:,:,1]
print(chips2)
print()

#布尔索引
boolArr = np.arange(0,100)
print(boolArr % 2 == 0) #比较完返回比较结果
print()

print(boolArr[boolArr %2 == 0])
print()

print(boolArr[boolArr > 10])
print()

print(boolArr[(boolArr % 2 == 0) & (boolArr > 10)])
print()

#花式索引
arrFlow = np.array([[1,2,3,4],[5,6,7,8]])
print(arrFlow[[-1,0]])


