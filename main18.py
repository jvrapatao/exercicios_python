import random
import string
# Escolha uma letra
pretendentes = 'Amanda', 'Carol', 'Maria', 'Ana'
h = input('Informe seu nome: ')
print('Possíveis pretendentes:')

for i in pretendentes:
    print (h, 's2', random.choice(pretendentes))
    
# Escolha um número de 1 a 10
print (random.randrange(1, 11))
# # Escolha um float no intervalo de 0 a 1
print (random.random())