number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))
number_3 = float(input('Введите третье число: '))


def my_func(arg_1, arg_2, arg_3):
    list_arg = [arg_1, arg_2, arg_3]
    min_arg = min(list_arg)

    list_arg.remove(min_arg)
    sum_arg = sum(list_arg)
    print(sum_arg)


my_func(number_1, number_2, number_3)