"""
* Enumerate - Enumerar elementos da lista # Lista
"""
lista = [
    # 0       1        2
    ['Edu', 'João', 'Luiz'],    # 0
    ['Maria', 'Aline', 'Joana'],    # 1
    ['Helena', 'Ed', 'Lu'],  # 2
]
enumerada = list(enumerate(lista))
print(enumerada[1][1])


"""
[ <-- Enumerate

    0   1
    (0,    ['Edu', 'João', 'Luiz'],    # 0
    (1,    ['Maria', 'Aline', 'Joana'],    # 1
    (2,    ['Helena', 'Ed', 'Lu'], # 2
]
"""
