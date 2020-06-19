print('Выход - Q, \nПродолжить - Enter: ')

sum_numbers = 0
exit_condition = True

while exit_condition:
    user_numbers = input('Введите числа через пробел: ')
    user_list = user_numbers.split()

    for user_value in user_list:
        if user_value.upper() == 'Q':
            exit_condition = False
            break
        try:
            f_number = float(user_value)
            sum_numbers += f_number
        except ValueError:
            print(user_value, 'не является числом')

    print('Сумма введенных чисел равна: ', sum_numbers)
