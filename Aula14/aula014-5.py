
operador = input('Escolha uma opção aritmética: som, sub, mult, div: ' )
num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

if num_1.isnumeric() or num_2.isnumeric():
    
    if operador == 'soma':
        resultado = num_1 + num_2
    if operador == 'sub':
        resultado = num_1 - num_2
    if operador == 'mult':
        resultado = num_1 * num_2
    if operador == 'div':
        resultado = num_1 / num_2
        print(f'O resultado da opeção é {resultado}.')

print('Digite apenas números!')
