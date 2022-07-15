import os
import time

print(__file__) #变量记录当前脚本的路径信息

print(__name__)

path = os.path.realpath(__file__)
print(path)

#filename
print(os.path.basename(__file__))

#pwd
print(os.path.dirname(__file__))
print(os.getcwd())

size = os.path.getsize('file/a.txt')
print(size)

#返回path的最后访问时间
atime = os.path.getatime('file/a.txt')
datea = time.localtime(atime)
print(time.strftime('%Y-%m-%d: %H:%M:%S',datea))

ctime = os.path.getctime('file/a.txt') #返回文件创建时间
datec = time.localtime(ctime)
print(time.strftime('%Y-%m-%d: %H:%M:%S',datec))

#返回最后的修改时间
mtime = os.path.getmtime('file/a.txt')
datem = time.localtime(mtime)
print(time.strftime('%Y-%m-%d: %H:%M:%S',datem))

#判断文件或者文件夹
fileList = os.listdir('D:\Code\Enterprise training\Coding\Python-Essential-Practice')
print(fileList)

print(os.path.isdir('D:\Code\Enterprise training\Coding\Python-Essential-Practice/'+fileList[4]))
print(os.path.isfile('D:\Code\Enterprise training\Coding\Python-Essential-Practice/'+fileList[2]))

#Python实现递归遍历文件系统
def fileTree(path,level):
    fileList = os.listdir(path)
    for filename in fileList:
        #os.sep根据你所处的平台，自动采用相应的分隔符号。 Linux系统某个路径，/usr/share/python,那么上面的os.sep就是'/' windows系统某个路径，C：\Users\Public\Desktop,那么上面的os.sep就是'\'.
        file = path + os.sep + filename
        if os.path.isdir(file):
            print('\t'*level +'>'+ file.split('\\')[-1])
            fileTree(file, level + 1)
        else:
            print('\t'*level + filename)
        ...
    ...

#课堂练习：递归实现文件系统遍历操作，打印成树形结构
print("Python-Essential-practice")
fileTree('D:\Code\Enterprise training\Coding\Python-Essential-Practice',0)

#创建和删除文件夹
try:
    os.mkdir('mkdir')
    os.rmdir('mkdir')
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
finally:
    print('操作完成')
    ...