
# texto = 'Python'
#
# for letra in texto:
#     print(letra)

# for n in range(10):
#     print(n)

texto = 'Python'

nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
