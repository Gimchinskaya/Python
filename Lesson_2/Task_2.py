# method_1

user_elements = input('Введите элементы списка через пробел: ')
user_list = user_elements.split()
print(user_list)

list_lenght = len(user_list)
k = 0

while k < list_lenght-1:
    user_list[k+1], user_list[k] = user_list[k], user_list[k+1]
    k += 2
print('Результат: ', user_list)

# method_2

for element in range(1, len(user_list), 2):
    user_list[element-1], user_list[element] = user_list[element], user_list[element-1]
print('Результат: ', user_list)





