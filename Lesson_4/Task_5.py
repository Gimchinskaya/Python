from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(my_list)


def my_func(prev_elem, elem):
    return prev_elem * elem


print('Произведение всех элементов списка: ', reduce(my_func, my_list))
