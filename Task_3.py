with open("for_task_3.txt", "r") as f:
    content = f.readlines()

    emp_low_salary = ''
    sum_salary = 0

    for line in content:
        employee_data = line.split()
        if len(employee_data) == 2:
            employee_surname = employee_data[0]
            employee_salary = int(employee_data[1])
            sum_salary += employee_salary
        else:
            print(f'В строке {employee_data.index(line) + 1} допущена ошибка, проверьте данные')

        if employee_salary < 20000:
            emp_low_salary += employee_surname + '\n'

    print(f'Фамилии сотрудников с зарплатой меньше 20 тыс.:\n{emp_low_salary}')
    print(f'Средняя величина дохода сотрудников: {sum_salary / len(content)}')
