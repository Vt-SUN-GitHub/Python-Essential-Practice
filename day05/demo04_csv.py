import csv
import pandas as pd

#写入csv数据
header = ['姓名','年龄','存款']
data = [['xu',21,1000.1],
        ['ma',21,999.1],
        ['fan',21,999.9]]

with open('file/data.csv',encoding='GBK',mode='w',newline= '') as fp:
    csvIO = csv.writer(fp)
    csvIO.writerow(header)
    csvIO.writerows(data)
    ...

with open('file/data.csv',mode='r',encoding='GBK', newline='') as fp:
    csvReader = csv.reader(fp)
    for line in csvReader:
        print(line)
        ...
    ...

df = pd.read_excel('file/message.xls')
print(df)
