n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
'''
if n1.isnumeric() and n2.isnumeric():
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)
else:
    print('Digite apenas números!')
'''

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)
else:
    print('Digite apenas números!')
