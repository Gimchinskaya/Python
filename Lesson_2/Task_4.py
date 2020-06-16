user_str = input('Введите несколько слов через пробел: ')
user_str_list = user_str.split()
user_str_numb = 1

for list_element in user_str_list:
    print(user_str_numb, list_element[0:10])
    user_str_numb += 1


