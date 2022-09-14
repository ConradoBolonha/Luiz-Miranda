
while True:
    n1 = input('Primeiro número: ')
    n2 = input('Segundo número: ')
    operador = input('Digite o operador aritmético: ')
    sair = input('Deseja sair? [s] ou [n]')
    
    if sair == 's':
        break
    
    if not n1.isnumeric() or not n2.isnumeric():
        print('Digite apenas números!')
        continue
        
    n1 = int(n1)
    n2 = int(n2)
    
    if operador == '+':
         print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n2)
    else:
        print('Digite apenas um operador aritimético!')
