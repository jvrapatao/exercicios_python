dias_percorridos = int(input('Quantos dias alugados: '))
km = float(input('Quantos KM rodados: '))
pago = (dias_percorridos * 60) + (km * 0.15)

print('O total a pagar é de: R${:.2f}'.format(pago))


