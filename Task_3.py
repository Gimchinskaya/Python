class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        print('Полное имя сотрудника: ', self.name + ' ' + self.surname)

    def get_total_income(self, employee_income_from_worker):
        print('Доход сотрудника с учетом премии: ', employee_income_from_worker['wage']
              + employee_income_from_worker['bonus'])


employee_name = input('Введите имя сотрудника: ')
employee_surname = input('Введите фамилию сотрудника: ')
employee_position = input('Введите должность сотрудника: ')
employee_wage = int(input('Введите оклад сотрудника: '))
employee_bonus = int(input('Введите премию сотрудника: '))

my_worker = Worker(employee_name, employee_surname, employee_position, employee_wage, employee_bonus)

employee_income = my_worker.get_income()

my_position = Position(employee_name, employee_surname, employee_position, employee_wage, employee_bonus)
my_position.get_full_name()
my_position.get_total_income(employee_income)

