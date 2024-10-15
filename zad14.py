x=3562
print(x%10)
print((x-x%10)/10%10)
suma=0
k=0
print((int)((x-x%10)/10%10))

for i in range(len(str(x))):
    k=x%10
    print(k)
    suma=suma+k
    x=x//10
print(suma)