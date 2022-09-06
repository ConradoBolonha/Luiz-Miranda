'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Exemplo: Das 0h as 12h, bom dia.
Das 13h as 17h, boa tarde e das 18h as 23h, boa noite.
'''

hora = input('Que horas são? (0 - 23): ')

if hora.isnumeric():
    hora = int(hora)
    
    if hora < 0 or hora > 24:
        print('Horário deve estar entre 0 e 24!')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
