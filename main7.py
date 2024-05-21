preco = float(input('Digite o preço do produto: R$'))
novo = preco - (preco * 5 / 100)

print('O produto que custava R${}, na promoção passou para R${}'
      .format(preco, novo))