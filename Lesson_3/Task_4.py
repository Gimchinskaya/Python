number_1 = float(input('Введите действительное положительное число x: '))
number_2 = int(input('Введите целое отрицательное число y: '))


def my_func(x, y):
    if (x > 0) & (y < 0):
        result_1 = x ** y
        print('Результат возведения X в степень y (способ 1): ', result_1)
    else:
        print('Вы ввели некорректные данные!')

    result_2 = 1
    while y < 0:
        result_2 = result_2 * (1 / x)
        y += 1
    print('Результат возведения X в степень y (способ 2): ', result_2)


my_func(number_1, number_2)



