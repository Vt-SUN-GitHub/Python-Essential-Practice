import matplotlib.pyplot as plt
import numpy as np
from day07_day08.jobBigData.jobBigData.dao.BaseDao import BaseDao
from day10.funcLibrary import randomColor

#用于正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

labels = ['Java', '机器学习', '大数据']

baseDao = BaseDao()

item =[]
colors = []

for label in labels:
    baseDao.execute("select count(*) from crawler_job where jobType = '"+label+"'")
    for value in  baseDao.fetchAll()[0].values():
        item.append(value)
        colors.append(randomColor())
    ...

for i in range(len(labels)):
    labels[i]+= ": "+(str)(item[i])
    ...


plt.pie(item, labels = labels, colors=colors)
plt.show()


