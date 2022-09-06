'''
Formatação de valores

:s - Texto(string)
    nome = 'Conrado'
    print(f'{nome:s}')
    
:d - Inteiros(int)
    num_1 = 5
    print(f'{num_1:d}')
    
:f - Número flutuante

### ALINHAMENTO ###

> - Alinha a esquerda
< - Alinha a direita
^ - Alinha no centro    

'''
num_1 = 10
num_2 = 3
div = num_1 / num_2
print(div)
print('{:.2f}'.format(div))
print(f'{div:.2f}')

num_3 = 199
print(f'{num_3:0>10}') #  Acrescenta sete zeros a esquerda
print(f'{num_3:0<10}') #  Acrescenta sete zeros a direta
