from functools import reduce

with open("for_task_5.txt", "w") as f:
    numbers = '20 30 40 50 60'
    f.writelines(numbers)

with open("for_task_5.txt", "r") as f_read:
    line = f_read.readlines()

    for elements in line:
        list_element = elements.split()
        number_el = [int(el) for el in list_element]

    print('Сумма чисел из файла: ', sum(number_el))
