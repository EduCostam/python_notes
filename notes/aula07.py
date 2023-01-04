nome = 'Eduardo'
idade = 24
altura = 1.74
e_maior = idade > 18
peso = 75
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'. format(nome, idade, imc))
print('{im} {n} tem {i} anos e seu imc é '.format(n=nome, i=idade, im=imc))
