
nome = str(input('Qual seu nome? '))
idade = int(input('Digite sua idade: '))
idade_menor = 20
idade_maior = 30
idade2 = """52"""

if idade >= idade_menor and idade <= idade_maior:
    print(f'O {nome} pode fazer empréstimo!')
else:
    print(f'Empréstimo não autorizado ao Sr. {nome}.')
