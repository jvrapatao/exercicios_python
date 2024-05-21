lista = ['A', 'B', 'C']
print('Fila:', lista)
# pop(0) com parâmetro remove o primiero e retorna o próximo "filas"
while lista:
    print('Saiu', lista.pop(0), 'faltam', len(lista))

print('_____________________\n')

lista += ['D', 'E', 'F']
print('Pilha:', lista)
# pop() sem parâmentro remove o último e retorna o próximo "pilhas"
while lista:
    print('Saiu', lista.pop(), 'faltam', len(lista))
