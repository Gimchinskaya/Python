revenue = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))


if revenue > costs:
    print('Фирма отработала с прибылью')
    rent = (revenue - costs)/revenue
    print('Общая рентабельность фирмы:', "%.3f" % rent)

    emp_number = int(input('Введите колличество сотрудников фирмы: '))
    emp_profit = (revenue - costs)/emp_number
    print('Прибыль на одного сотрудника:', "%.3f" % emp_profit)
else:
    print('Фирма отработала в убыток')


