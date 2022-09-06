nome = 'CoNrAdo'
sobrenome = 'BoLOnHa'

print('{0:#^13}'.format(nome, sobrenome))
print('{0:#>10} {1:#<10}'.format(nome, sobrenome))
print(f'{sobrenome:@>10}')

print(nome.upper())
print(nome.lower())
print(nome.title(), sobrenome.title())

palavra = input('Digite uma palavra: ')
print(palavra.isupper())
