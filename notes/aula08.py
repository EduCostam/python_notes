"""
*Criar variáveis para nome (str), idade (int),
*Altura (float) e peso (float) de uma pessoa
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80
ano_atual = 2019
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos,', altura, 'de altura e pesa', peso, 'kg.')
print(f'{nome} O IMC de Luiz é {imc:.2f}')
print('Luiz nasceu em', ano_atual - idade)

# Correção do exercício

nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80
ano_atual = 2019
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
