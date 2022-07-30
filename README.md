# Python-Essential-Practice

2022 Python机器学习代码汇总（课程练习代码+课程作业代码）:sunny:

## 前言
代码可供参考和借鉴，如有~~（实在看不起下去的）~~错误欢迎指正。

## 编译环境 
>+ Python version：3.9.5+
>+ IDE：Pycharm Community Edition 2019+

## 项目结构

python模块  | 文件夹  | 作业内容 | 当前进度
 :----: | :-----: | :------:  | :-------: |
 numpy+matplotlib | day10 | 网站数据可视化展示 | 完成 |
 
## 联系方式
 - sun_flower@bupt.edu.cn  (欢迎来骚扰~) :cherry_blossom:

## 代码解读
### [day10]
~~**`import numpy as np`**~~

~~**`~~import matplotlib.pyplot as plt~~`**~~
- [x] demo01_np_func

- `np.exp(), np.where(), np.add()/subtract(), np.power(), np.modf(), np.log(),
 np.where(), np.any()/all(), np.sort(), np.unique()`
 
- [x] demo02_np_math

- `np.sum(array, axis=0/1), np.argmax()`

- [x] demo03_np_lina
- `np.dot(), np.linalg.eig(), np.linglg.inv(), np.meshgrid()`

- [x] demo04_matplotlib_lineChart
-  `plt.plot(), plt.show()`

- [x] demo05_matplotlib_barGraph
- `plt.subplot(), .title(), .set_xlabel(), .set_ylabel(), .set_xticks()
, .set_xticklabels(), .bar().set_color()`
- `plt.text(), plt.grid(linestyle='--')`

- [x] demo06_matplotlib_pieChart
- `plt.pie(), 获取MySQL中按职位类型统计职位的个数，利用饼状图显示`

- [x] demo07_matplotlib_scatterChart
- `plt.scatter(rand[:,0], rand[:,1], s=40, c=randomColor(), alpha=0.5, marker="v")`
- `s:散点面积, c:散点颜色, marker:散点样式(v,o), alpha → 散点透明度`

- [x] demo08_matplotlib_subplot
- `plt.figure().add_subplot() 多个子图表显示`

- [x] demo09_matplotlib_wordcloud
- `获取QQ聊天记录词云图 QQ消息管理 -> 右键联系人 -> 导出消息记录 -> 保存为文本文件`
- `在处理脏数据部分可进行修改（看两个人的聊天习惯，可添加屏蔽其它系统消息）`
- `如果系统字体中没有SimHei.ttf，可下载该字体或选择其它支持中文的字体`

- [x] Homework_10
- `Github社区python项目数据分析 + 统计分析猎聘网站的数据，并进行可视化展示`
- `使用API调用数据 -> 处理APU响应 -> 利用pyplot可视化`
![Homework_10效果图](https://github.com/Vt-SUN-GitHub/Python-Essential-Practice/blob/main/day10/Homework10_result.png)

