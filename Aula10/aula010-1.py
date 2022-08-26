
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

'''
n1 = int(n1) #  Converte n1 em int
n2 = int(n2) #  Converte n2 em int
'''

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)

    print(n1 + n2)
else:
    print('Digite somente números!')
