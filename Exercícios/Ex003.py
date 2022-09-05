'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Exemplo: Das 0h as 12h, bom dia.
Das 13h as 17h, boa tarde e das 18h as 23h, boa noite.
'''

hora = input('Que horas são? ')
if hora.isnumeric():
    hora = int(hora)
    if hora > 0 and hora < 12:
        print('Bom dia!')
    elif hora > 13 and hora < 17:
        print('Boa tarde!')
    elif hora > 18 and hora < 23:
        print('Boa noite!')
else:
    print('Digite apenas números inteiros!')
