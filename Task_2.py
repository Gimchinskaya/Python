class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_of_mass(self):
        """ масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см (в кг)"""
        mass = 25
        """ число см толщины полотна"""
        thickness = 5
        print(f'Масса асфальта {self._length} м * {self._width} м * {mass} кг * {thickness} см =',
              self._length * self._width * mass * thickness // 1000, 'т')


user_length = int(input('Введите длину полотна: '))
user_width = int(input('Введите ширину полотна: '))

my_road = Road(user_length, user_width)
my_road.calculation_of_mass()
