'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos, escreva "Seu nome é curto". Se tiver entre 5 e 6 caracteres, escreva
"Seu nome é normal". Maior que seis caracteres, digite "Seu nome é grande".
'''

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto!')
elif tamanho_nome <= 6:
    print('Seu nome é comum!')
else:
    print('Seu nome é grande!')