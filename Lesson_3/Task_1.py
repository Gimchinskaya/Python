number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))


def my_division(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
    except ZeroDivisionError:
        return print('Деление на 0 недопустимо!')
    return print('Результат деления первого числа на второе: ', result)


my_division(number_1, number_2)

