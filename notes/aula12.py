"""
O bloco elif é usado quando se faz necessário checar outras condições ou variações
da mesma condição. O bloco elif depende do cloco if, ou seja, é necessário primeiro
usar o bloco if e somente se a expressão do bloco if for falsa, o bloco elif será verificado.

O bloco else só é executado quando nenhuma condição de if ou elif for verdadeira.
Por isso, quando precisamos de um valor padrão ou de uma resposta contrária á condiçãom é necessário
adicionar o bloco else.
"""
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos. ')

"""
Operadores Lógicos - Aula 12
and, or, not
in e not in
"""
# (Verdadeiro E Verdadiero) = Verdadeiro
# (Verdadeiro E False) = Falso
# comparacao1 and comparacao2

# Verdadeiro OU Verdadeiro
# comp1 OR comp2

a = 2
b = 3

if b > a:
    print('B é maior do que A. ')
else:
    print('A é maior do que B. ')
