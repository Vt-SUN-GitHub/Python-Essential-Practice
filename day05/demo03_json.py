import json

dict1 = {'name':'xu', 'age': 21, 'university': 'whu'}
jsonStr = json.dumps(dict1, ensure_ascii=False) #输出真正的中文 需要ensure_ascii = False
print(jsonStr)

with open("file/data.json", mode='w') as fp:
    fp.write(jsonStr)
    ...

data = [{'name':'xu', 'age': 21, 'university': 'whu'},
        {'name':'ma', 'age': 20, 'university': 'yin'},
        {'name':'fan', 'age': 19, 'university': 'ning'}]
jsonData = json.dumps(data, ensure_ascii=False)

with open('file/data1.json', mode='w') as fp:
    fp.write(jsonData)
    ...

#json字符串 转Python对象
with open('file/data1.json', mode='r') as fp:
    data = json.load(fp) #从json文件读取json
    print(data)
    print(type(data))
    ...

print(json.loads(jsonData))