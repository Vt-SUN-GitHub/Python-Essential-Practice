#代码缩进
a = 1
b = 2
if a >= 1 and b >= 2 :
    c = a + b
    d = a - b
    if c > d:
        print(c)
    pass#补全和代码格式优化

class demo:
    pass

class demo2:
    ...


#注释和字符串
name = '张三'
print(type(name))#<class 'str'>
sex = "男"
print(type(sex))#<class 'str'>
address = str("北京")
print(type(address))
text = """春天已经来了
冬天还会远吗"""
print(text)

def sum(x,y):
    '''
    :param x: x is addend
    :param y: y is addend
    :return: sum
    '''
    return x+y


print(str(10)+"a")
print(10,"c")

print("www","taoju","tv",sep=".")

if __name__ == '__main__':
    print("entrance")
    print(sum(1,2))
    pass