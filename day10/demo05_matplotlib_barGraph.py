import matplotlib.pyplot as plt
import numpy as np
from day10.funcLibrary import randomColor

month = [1,2,3,4,5,6,7,8,9,10,11,12]
sell = np.random.randint(5000,10000,size=12)

#用于正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

#添加画布
plt.title('月销售额统计')
subplot = plt.subplot()
subplot.set_xlabel('月份')
subplot.set_ylabel('销售额/万元')

#设置X轴的每个标签的具体位置为每个柱子的中央
subplot.set_xticks(month)
#设置每个标签的名字
subplot.set_xticklabels(month)

bars = subplot.bar(month,sell)

for bar in bars:
    bar.set_color(randomColor())
    ...

for x, y in zip(month, sell):
    plt.text(x, y + 0.05, str(y)+"万元", ha='center', va='bottom')
    ...

plt.plot(month, sell, randomColor())

plt.grid(linestyle='--')
plt.show()