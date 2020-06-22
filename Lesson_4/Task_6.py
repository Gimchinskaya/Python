from itertools import count, cycle
print('Пример использования функции count:')
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

print('Пример использования функции cycle:')
i = 0
for el in cycle('qwer'):
    if i == 10:
        break
    print(el)
    i += 1
