salario = int(input('Salário: '))
imposto = input('Imposto: ')

if imposto == '':
    imposto = 0.27
else:
    imposto = float(imposto)


valor_descontado = salario - (salario * imposto) - salario
novo_salario = salario - (salario * imposto)

print('Valor descontado: {}'.format(valor_descontado))
print('salario atual com imposto: {}'.format(novo_salario))

