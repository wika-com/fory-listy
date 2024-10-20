t=[0,2,4,6,80]
s=[0,10,20,40,600]
j=0
for i in t:
    if i==0:
        print("czas:", i,"położenie", s[j],"prędkość", i)
    else:
        print("czas:", i,"położenie", s[j],"prędkość", i/s[j])
    j=j+1