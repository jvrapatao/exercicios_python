qtd = 0
soma = 0
media = 0
valor = float(input(f'Digite um valor: '))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    media = soma/qtd
    valor = float(input(f'Digite um valor: '))

print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(f'Total da soma: %.1f' % soma)
print(f'Quantidade dos valores digitados: %.1f' % qtd)
print(f'Média dos valores: %.1f' % media)
