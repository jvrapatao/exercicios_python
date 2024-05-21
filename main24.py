lista = [1, 2, 3, 4]

print(format(len(lista)))
print(lista[0])
print(lista[-1])
print(lista[1:3])

lista.append(5)
print(lista)

lista[4] = 'cinco'
print(lista)
# if avalia uma lista vazia como falsa
if lista == '':
    print('Lista vazia')
else:
    print('Lista preenchida')

for x in lista:
    print(x)


lista2 = ['um', 'dois', 'três', 'quatro', 'cinco']
for l in lista2:
    if l.startswith('u'):
        continue
    print(l.upper())

for y in range(6):
    print(y)

r = range(5)
print(r)


for ind, n in enumerate(lista):
    print(ind, n)
    
    
