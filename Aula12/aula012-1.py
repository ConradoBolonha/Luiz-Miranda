'''
<<<<<<< HEAD
### Formatação de valores com modificadores ###
=======
Formatação de valores
>>>>>>> 89b7f2a9beda540b2c7ebe13c4218f1c977bc982

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
print(f'{num_3:0^10}') #  Coloca o número 10 no centro
print(f'{num_3:.2f}') #  Tranforma o número inteiro 199 em float (199.00)
print(f'{num_3:0<10.2f}')
