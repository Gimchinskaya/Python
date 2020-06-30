class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки\n')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой\n')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом\n')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером\n')


my_stationery = Stationery('канцелярская принадлежность')
print(my_stationery.title)
my_stationery.draw()

my_pen = Pen('ручка')
print(my_pen.title)
my_pen.draw()

my_pencil = Pencil('карандаш')
print(my_pencil.title)
my_pencil.draw()

my_handle = Handle('маркер')
print(my_handle.title)
my_handle.draw()
