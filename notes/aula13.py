string1 = input('Digite alguma coisa: ')
string2 = input('Digite alguma coisa: ')

print(
    f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você preisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema. ')
