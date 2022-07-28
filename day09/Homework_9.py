'''
1.	（必做） 读取 iris.csv数据，抽取数据部分的内容
a)	数据采集
使用loadtxt函数读取csv数据（iris.csv）
b)	数据抽取
抽取数据部分内容（去掉标题行），同时将数据全部转换成float64类型
c)	数据保存
将分片抽取后的数据使用savetxt保存成 iris_data.csv
d)	再次读取 iris_data.csv数据显示
'''

import numpy as np

irisArray = np.loadtxt('./iris.csv',dtype=float,delimiter=',',skiprows=1)
print(irisArray)
print()

np.savetxt('./iris_data.csv',irisArray, delimiter=',', fmt='%.1f')
print(np.loadtxt('./iris_data.csv',dtype=float, delimiter=','))
