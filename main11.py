from math import trunc, ceil

num = float(input("DIgite um número: "))

print(' O número {} tem a porção inteira de: {}'
    .format(num, trunc(num)))

print('O número {} foi arredondado para cima: {}'
    .format(num, ceil(num)))

