from math import factorial

user_number = int(input('Введите число: '))


def fact(n):
    for n in range(1, n + 1):
        yield factorial(n)


print(fact(user_number))

i = 1
for el in fact(user_number):
    if i <= user_number:
        print(f'{i}! = {el}')
        i += 1
