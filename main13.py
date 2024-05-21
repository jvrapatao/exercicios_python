nome = str(input('Digite seu nome completo: ')).split()

print('Seu nome tem ao todo {} letras'
      .format(len(nome) - nome.count(' ')))
