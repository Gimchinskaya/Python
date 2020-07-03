class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        if self.quantity is not None:
            return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return Cell(self.quantity - other.quantity)
        else:
            print('Отрицательно значение разности!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


my_cell = Cell(7)
sec_cell = Cell(6)

print(my_cell + sec_cell)
print(my_cell - sec_cell)
print(my_cell * sec_cell)
print(my_cell / sec_cell)

print(my_cell.make_order(5))
print((my_cell * sec_cell).make_order(5))