def lerNotas():
    n = float(input("Digite a nota do aluno(x): "))
    return n


def resultado(n1, n2):
    media = (n1 + n2)/2
    print('Nota 1: ',n1)
    print('Nota 2: ', n2)
    print('Média: ', media, 'Resultado: ', end='')
    if media >= 7:
        print('AP')
    else:
        print('RP')


a = lerNotas()
b = lerNotas()
resultado(a,b)