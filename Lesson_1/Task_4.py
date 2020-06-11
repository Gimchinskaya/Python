value = -1
max_num = 0
while value < 0:
    value = int(input('Введите число: '))
    if value < 0:
        print('Число введено неверно, попробуйте еще раз')
    else:
        while value > 0:
            num = value % 10
            value = value//10
            if num > max_num:
                max_num = num
print('Самая большая цифра в числе:', max_num)