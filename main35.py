faturamento = 1500
custo = 500
lucro = faturamento - custo
print(f'O lucro foi de R${lucro:,.2f}')


margem = lucro / faturamento
print(f'A margem foi de: {margem:.2%}')

lucro_formato_br = f'R${lucro:_.2f}'
lucro_formato_br = lucro_formato_br.replace('.', ',').replace('_', '.')
print(f'O lucro foi de: {lucro_formato_br}')
