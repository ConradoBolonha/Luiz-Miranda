nome = 'Conrado'
idade = 45
altura = 1.82
peso = 95
e_maior = idade > 18
imc = peso / altura ** 2

'''
print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('Maior de 18 anos? : ', e_maior)
print('Peso: ', 95)
'''
print(f'\n{nome}, você tem {idade} de idade, pesa {peso} e seu IMC é {imc:.2f}') #  .format(nome, idade, peso, imc))
print('{}, você tem {} de idade, pesa {} e seu IMC é {:.2f}'.format(nome, idade, peso, imc))
print('{n}, você tem {i} de idade, pesa {p} e seu IMC é {im:.2f}\n'.format(n=nome, i=idade, p=peso, im=imc))
