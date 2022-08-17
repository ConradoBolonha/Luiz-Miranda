print()
usuario = input('Digite o nome de usuário: ')
senha = input('Senha? ')

usuario_bd = 'conradobolonha'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado!')
else:
    print('Usuário ou senha inválido!')
print()
