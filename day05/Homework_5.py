'''
1.	（必做）函数编程，实现各种数据文件格式互相转换的功能脚本。
要求：
a.	定义函数 jsonToCsv(……)实现json文件转换成csv格式的文件
b.	定义函数 csvToJson(……)实现csv格式的文件转换成json文件
'''
import csv
import json

def jsonToCsv(file,newFile):
    data = []
    with open(file,mode='r',) as fp:
        str = json.load(fp)
        if type(str) == list:
            header = str[0].keys()
            for item in list(str):
                data.append(list(item.values()))
        if type(str) == dict:
            header = str.keys()
            data = list(str.values())
        ...
    with open(newFile, mode='w',encoding='GBK',newline='') as fp:
        csvIO = csv.writer(fp)
        csvIO.writerow(header)
        if type(data[0]) != list:
            csvIO.writerow(data)
            ...
        else:
            csvIO.writerows(data)
            ...
        ...
    ...

def csvToJson(file, newFile):
    data = []
    with open(file, mode='r',encoding='GBK', newline='') as fp:
        csvReader = csv.reader(fp)
        for line in csvReader:
            data.append(line)
            ...
        ...
    jsonData = []
    singleJsonData = {}
    for i in range(len(data)): #i 有几组json数据
        for j in range(len(data[0])): #每组json数据有几个元素
            singleJsonData[data[0][j]] = data[i][j]
            ...
        jsonData.append(singleJsonData)
        ...

    with open(newFile,mode='w', encoding='GBK') as fp:
        dumpData = json.dumps(jsonData,ensure_ascii=False)
        fp.write(dumpData)
        ...
    ...

if __name__ == '__main__':
    jsonToCsv('file/data1.json','file/jsonToCsv.csv')
    csvToJson('file/data.csv','file/csvToJson.json')
    ...

