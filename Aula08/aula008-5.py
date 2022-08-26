print()
usuario = input('Digite o nome de usuário: ')
senha = input('Senha? ')

usuario_bd = ['cbolonha', 'osaka']
senha_bd = '123'

if usuario in usuario_bd and senha == senha_bd:
    print('Você está logado!')
else:
    print('Usuário ou senha inválido!')
print()
