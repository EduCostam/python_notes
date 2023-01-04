import re


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^\-{,1}[0-9]+$', val):
        return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('Digite um número ')
num2 = input('Digite um número ')

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print('ERROR')

num1 = input('Digit um número: ')
num2 = input('Digite outro número: ')

# num1 = int(num1)
# num2 = int(num1)

# isnumereric isdigit isdecimal
# números e positivos (123456)
# print(num1.isnumeric())
# print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter os número para ralizar condas. ')
