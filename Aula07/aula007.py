# Usando o comando "input".

nome = str(input('Qual seu nome: '))
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2

print(f'Seu nome é {nome} e você tem {idade} anos de idade, peso {peso} e seu IMC é {imc:.2f}.')
print(f'Seu nome {nome}')