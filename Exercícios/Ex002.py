'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro.
'''

num = input('Digite um número: ')

if num.isnumeric():
    num = int(num)
    if num % 2 ==0:
        print(f'Você digitou o número {num} e esté é "PAR".')
    else: print(f'Você digitou o número {num} e este é "ÍMPAR".')
else:
    print ('Digite apenas números inteiros!')
