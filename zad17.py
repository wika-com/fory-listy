
m=0
for i in range(2,101):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k==2:
        print(i)
        m=m+1
print(m)