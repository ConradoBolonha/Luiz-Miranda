'''
1-Criar variáveis para nome (str), idade (int), altura (float) e peso (bool).
2-Criar variável com o ano atual (int).
3-Obter o ano de nascimento da pessoa (baseado na idade e no ano atual).
4-Obter o IMC da pessoa com duas casas decimais (peso e na altura da pessoa).
5-Exibir um texto com todos os valores na tela usando F-Strings (com as chaves).
'''

#  Resposta exercícios 1 e 2:
nome = 'Conrado'
idade = 45
altura = 1.82
peso = 95
ano_atual = 2022
print(nome, idade, altura, peso, ano_atual)

#  Resposta exercício 3:
idade_pessoa = ano_atual - idade
print('Resposta exercício 3 --> ', end='')
print(idade_pessoa)

#  Resposta exercício 4
imc = peso / altura ** 2
print('Resposta exercício 4 --> ', end='')
print(f'{imc:.2f}')

#  Resposta exercício 5
print(f'Seu nome é {nome}, você tem {idade} anos, sua altura é de {altura} e seu IMC é {imc:.2f}')
