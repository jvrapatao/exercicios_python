print("""\
uso: consulta_base
    -h              exibe...
    -U url          Url...
""")

string = u'string unicode'
print(len(string))
print(string[::-1])
print('n' in string)
print('n' in 'string')
print('m' not in string)
print('s' + 'tring')
print('a' * 3)

new_string = string[0:13] + '1'
print(new_string)

new_string = string.replace('e', '1')
print(new_string)

print(string.capitalize())
print(string.count('i'))
print(string.startswith('s'))
print(string.endswith('m'))
print(string.split(' '))
join_string = ' '
print(join_string.join(['string', 'join']))

# interpolacao_string = '%s string interpolada' % ('uma')
interpolacao_string = '%d string interpolada' % (1)
print(interpolacao_string)

interpolacao_string = '{} string interpolada'
print(interpolacao_string.format(1))

interpolacao_string = '{uma} string interpolada'
print(interpolacao_string.format(uma=1))

