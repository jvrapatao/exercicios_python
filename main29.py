
with open('Arquivo.txt', 'w+') as arquivo:
    arquivo.write('Aquivo A')
    arquivo.seek(0)
    print(arquivo.read())
