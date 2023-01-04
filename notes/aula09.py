"""
Entrada de dados - Aula - 9
A função input sempre retorna uma string, independente do que for digitado pelo usuário
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2022-int(idade)

print()
print(f'O usuário digitou {nome} e o tipo da variável é'
      f'{type(nome)}')
print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {ano_nascimento}.')
