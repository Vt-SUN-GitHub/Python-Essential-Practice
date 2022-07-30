'''
任务1. GitHub官方代码仓库关注度可视化。
任务2. 统计分析猎聘网站的数据，并进行可视化展示。
'''

from day10.funcLibrary import randomColor
import matplotlib.pyplot as plt
import numpy as np
from day07_day08.jobBigData.jobBigData.dao.BaseDao import BaseDao
import requests
import sys

#使用response模块的get(url)方法访问获取网络数据
def getRespData():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('无法获取网站数据')
        sys.exit()

#读取MySQL数据库中的数据
def getMySQLData(sql):
    baseDao = BaseDao()
    baseDao.execute(sql)
    return baseDao.fetchAll()

#用于正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

#显示两张图表
figure = plt.figure()
githubFigure = figure.add_subplot(2,1,1)
jobFigure = figure.add_subplot(2,1,2)

#任务1: Github官方代码仓库关注度可视化
response_dict = getRespData()
repo_dicts = response_dict['items']
names = [repo_dict['name'] for repo_dict in repo_dicts]
plot_dicts = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]
#用于正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#横轴的点数
x = np.arange(len(names))
bars = githubFigure.bar(x,plot_dicts)

# 给每个bar分配随机的颜色
for bar in bars:
    bar.set_color(randomColor())
    ...

githubFigure.set_title('GitHub官方代码仓库关注度可视化')
# githubFigure.set_xlabel('仓库名')
githubFigure.set_ylabel('关注度')
githubFigure.set_xticks(x)
githubFigure.set_xticklabels(names)
githubFigure.plot(x,plot_dicts,randomColor())

# 为每个柱状块添加具体文字数据
for z, y in zip(x, plot_dicts):
    githubFigure.text(z, y+0.05, y, ha='center', va='bottom')
    ...

#任务2. 统计分析猎聘网站的数据，并进行可视化展示。
allCities = []
cities = []
JavaMeanSalary = []
BigDataMeanSalary = []
PythonMeanSalary = []
for value in getMySQLData('select jobCity from crawler_job'):
    for city in value.values():
        allCities.append(city)
        ...
    ...

#保留唯一的城市名
for city in allCities:
    if city not in cities:
        cities.append(city)
        ...
    ...

#按城市获取三种岗位的平均薪资
for city in cities:
    for value in getMySQLData("SELECT AVG(jobMeanSalary) FROM crawler_job where jobCity = '"+city+"' and jobType = 'Java'"):
        for salary in value.values():
            javaSalary = salary
            ...
        ...
    for value in getMySQLData("SELECT AVG(jobMeanSalary) FROM crawler_job where jobCity = '"+city+"' and jobType = '大数据'"):
        for salary in value.values():
            pythonSalary = salary
            ...
        ...
    for value in getMySQLData("SELECT AVG(jobMeanSalary) FROM crawler_job where jobCity = '"+city+"' and jobType = '机器学习'"):
        for salary in value.values():
            bigDataSalary = salary
            ...
        ...
    JavaMeanSalary.append(javaSalary) if javaSalary else  JavaMeanSalary.append(0)
    BigDataMeanSalary.append(bigDataSalary) if bigDataSalary else BigDataMeanSalary.append(0)
    PythonMeanSalary.append(pythonSalary) if pythonSalary else PythonMeanSalary.append(0)
    ...

#绘图
cx = np.arange(len(cities))
jobFigure.plot(cx, JavaMeanSalary, 'bp-', alpha=0.5, label='Java')
jobFigure.plot(cx, BigDataMeanSalary, 'mp-', alpha=0.5, label='大数据')
jobFigure.plot(cx, PythonMeanSalary, 'yp-', alpha=0.5, label='机器学习')

jobFigure.set_title('各城市不同种类岗位的平均薪资')
jobFigure.set_xlabel('城市')
jobFigure.set_ylabel('平均薪资')
jobFigure.set_xticks(cx)
jobFigure.set_xticklabels(cities)

#显示图表
plt.legend(loc='best')
plt.grid(linestyle='--')
plt.show()