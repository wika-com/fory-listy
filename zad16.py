lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=lista1[:]

for i in lista1:
    for j in lista2:
        print(i, "*", j, "=", i*j)