lista=[2,4,6,23,14,2,56,8]
minn=100
maxx=0
for i in lista:
    if i<minn:
        minn=i
    if i>maxx:
        maxx=i
print(minn, maxx)