x=23
k=0
for i in range(2,x):
    if x%i==0:
        print("x nie jest liczba pierwsza")
        break
    else:
        k=k+1
if k==(x-2):
    print("x jest liczba pierwsza")