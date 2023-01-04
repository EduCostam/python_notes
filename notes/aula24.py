"""
For / Else em Python
"""
variavel = ['Luis Otávio', 'Joãozinho', 'Maria']
#
# for valor in variavel:
#     if valor.startswith('J'):
#         print('Começa com J', valor)
#     else:
#         print('Não Começa com J', valor)

comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')
