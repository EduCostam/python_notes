"""
Operadores Relacionais - Aula 11
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""
print(2 == 1)

num_1 = 2  # int
num_2 = 2  # int

expressao = (num_1 >= num_2)

print(expressao)

var_1 = 'Eduardo'
var_2 = 'Otavio'

print(var_1 != var_2)
print(expressao)

nome = input('Qual o seu nome? ')
idade = input('Qaul a sua idade? ')

idade = int(idade)

# Limite para pegar empréstimo
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} NÃO pode pegar o empréstimo. ')
