from random import choice

lista = []

for nomes in range(4):
    nomes = input('Irforme seu nome: ')
    lista.append(nomes)

print('O nome escolhido foi: "{}"' .format(choice(lista)))
