import math

lista=[]
m=0
for i in range(1,51):
    for j in range(i,51):
        k=i*i+j*j
        k=math.sqrt(k)
        if k<50 and k==int(k):
            print(i, j, k)
            m=m+1
print(m)