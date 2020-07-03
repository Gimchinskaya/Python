from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothing):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def cloth_consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Clothing):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def cloth_consumption(self):
        return 2 * self.h + 0.3


my_coat = Coat("пальто", 48)
cloth_coat = float('{:.2f}'.format(my_coat.cloth_consumption()))

my_costume = Costume("костюм", 183)
cloth_costume = my_costume.cloth_consumption()

sum_tissue_consumption = cloth_coat + cloth_costume
print(cloth_coat)
print(cloth_costume)
print(sum_tissue_consumption)