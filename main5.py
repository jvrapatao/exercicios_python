arquivo = open('arqText.txt', 'w')

arquivo.write('Aprendizado \n')
arquivo.write('Python')
arquivo.close()

# Leitura do arquivo texto

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()