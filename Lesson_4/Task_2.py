my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список: {my_list}')
result = [my_list[el] for el in range(len(my_list)-1) if (el > 0) & (my_list[el] > my_list[el - 1])]
print(f'Элементы исходного списка, значения которых больше предыдущего элемента: {result}')
