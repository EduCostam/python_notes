"""
Iniciar com letra, pode conter números, separar _. letras minúsculas.
Strings são qualquer texto entre aspas simples, aspas duplas, aspas simples
triplas e aspas duplas triplas. Int são números inteiros negativos ou positivos
(fora de aspas). Float são números com ponto flutuante (fora de aspas). Valores booleanos
(lógicos) só podem ter dois valores, True para verdadeiro e False para falso.
"""
nome = 'Eduardo'
idade = 24
altura = 1.74
e_maior = idade > 18
peso = 75
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print(idade * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

nome = 'Joãozinho'
idade = """40"""
peso = 80.5
e_maior

print(nome, 'tem', idade, 'anos e pesa', peso, 'quilos')
print(nome, 'é maior de idade?', e_maior)
