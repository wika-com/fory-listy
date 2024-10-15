
for i in range(1,101):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k==2:
        m=i+2
        p=0
        for n in range(1, m + 1):
            if m%n==0:
                p=p+1
        if p==2:
            print(i,m)