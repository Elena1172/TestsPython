def unicc(*arg,k = False):
    x = []
    for i in arg:
        for j in i:
            if j  not in x:
                x.append(j)
    if k == True:
        x.sort()
        return (x)
    return (x)
c = [-2,55,8,9,10,-55]
b = [8,9,10,-100]
l = [9,8,100,]
y = unicc(c,b,l)
print(y)
y = unicc(c,b,l,k = True)
print(y)