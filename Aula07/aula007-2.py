print()
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
ano_nasc = 2022 - idade

print(f'Seu nome é {nome} e é uma {type(nome)}, idade é uma {type(idade)} e peso é {type(peso)}.')
print(f'Você tem {idade} anos e '
      f'nasceu no ano de {ano_nasc}.')
print()
