list2D = [1,2,3,4],[5,6,7,8]

for row in list2D:
    for col in row:
        print(col,end=",")
    print()
    ...

for i in range(len(list2D)):
    for j in range(len(list2D[i])):
        print(list2D[i][j],end=",")
        ...
    print()
    ...

i = 0
while i < 10:
    i += 1
    pass
print(i)