import os

#二进制文件的读写
ioObj = open('file/star.png', 'rb')
data = ioObj.read()
print(data)
ioObj.close()

#追加写文本文件
file = open('file/a.txt', 'a+', encoding='UTF-8') #得到文件对象
file.write('aaaa\n')
file.flush()
file.close()

writeIO = open('file/a.txt', mode='a+', encoding='utf-8')
writeIO.write('好好学习，天天向上\n')
writeIO.flush()
writeIO.close()

#读文本文件
readFile = open('file/a.txt', 'r', encoding='utf-8')
text = readFile.read()
print(text)

