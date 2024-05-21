s = int(input("Salário: "))
i = 0.27

while i <= 1:
    i = input('Ao informar o imposto o salário atualizará com o desconto'
              'ou (s) para sair: ')
    if not i:
        i = 0.27
    elif i == 's':
        print('----Obrigado----')
        break
    else:
        i = float(i)
    print('Valor: R${}'.format(s - (s*i)))

