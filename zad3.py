from audioop import reverse

lista=[5, 10, 15, 20, 25, 30]
lista.append(35)
'''print(len(lista))
print(lista[1:5])
print(lista[:-1])
'''

print(lista[::-1])
lista.pop(len(lista)//2)
print(lista)
print(max(lista))
print(sum(lista))
print("średnia:", sum(lista)/len(lista))