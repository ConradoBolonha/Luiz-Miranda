palavra = input('Digite uma palavra: ')
cont_palavra = len(palavra)
if palavra.isalpha():
    print(f'Você digitou a palavra {palavra}.')
    print(f'Essa palavra tem {cont_palavra} letras.')
    print(f'A palavra em maiúsculo ficou {palavra.upper()}')
else:
    print('Digite apenas letras!')
