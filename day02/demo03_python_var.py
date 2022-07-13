#变量的使用

#相同的值节省内存空间
a = 1
c, b = 1, 1

print(id(a))

print(id(b))
print(id(c))

a = 2

print(id(a))

print(b)