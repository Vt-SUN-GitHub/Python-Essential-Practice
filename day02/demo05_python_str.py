#字符串类型
str = 'I love China!'

#索引（正负，切片）
print(str[0])
print(str[-1])
print(str[-2])
print(len(str))
print(str[2:6:1])#上界和下界面，步长，不包含上界[2,6)
print(str[0::2])#从零号位开始，以间隔2取出

print(str*2)

print('love' in str)
print('love' not in str)

print(str.count('I'))

#按区域查询
print(str.count('i',1,3))

#结束
if str.endswith('!'):
    print(True)
    ...

print(str.find("China"))

#健壮性，返回-1
print(str.find("Japan"))

print(str.index("China"))

#报错
# print(str.index("find"))

#替换字符串
str1 = str.replace("love", "live in")
print(str1)

#分割字符串
print(str.split(" "),str1.split(" "))

#strip() == trim() 用于移除字符串头尾指定的字符（默认为空格）
name = "  zhangSan"
print(name.strip())

