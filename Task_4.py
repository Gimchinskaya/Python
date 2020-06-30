class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.set_police(is_police)

    def set_police(self, is_police):
        if is_police == 'police':
            self.is_police = True
        else:
            self.is_police = False

    def go(self):
        if self.speed > 0:
            print('Car rides!')

    def stop(self):
        if self.speed == 0:
            print('Car stay')

    def turn(self, direction):
        if direction == 'forward':
            print(self.name, 'rides forward')
        if direction == 'back':
            print(self.name, 'rides back')
        if direction == 'left':
            print(self.name, 'rides to the left')
        if direction == 'right':
            print(self.name, 'rides to the right')

    def show_speed(self):
        print(f'Speed of Car {self.name} = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed of Car is {self.speed}. It is speeding!!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed of {self.name} is {self.speed}. It is speeding!!!')


class PoliceCar(Car):
    pass


my_car = TownCar(70, 'red', 'reno', 'not police')
print('\nName of my Car:', my_car.name)
print('Speed of my Car:', my_car.speed)
print('Color of my Car:', my_car.color)
print('Police type of my Car:', my_car.is_police)

my_car.show_speed()
my_car.go()
my_car.stop()
my_car.turn('left')

my_car = SportCar(120, 'blue', 'bmw', 'not police')
print('\nName of my Car:', my_car.name)
print('Speed of my Car:', my_car.speed)
print('Color of my Car:', my_car.color)
print('Police type of my Car:', my_car.is_police)

my_car.show_speed()
my_car.go()
my_car.stop()
my_car.turn('right')

my_car = PoliceCar(80, 'grey', 'ford', 'police')
print('\nName of my Car:', my_car.name)
print('Speed of my Car:', my_car.speed)
print('Color of my Car:', my_car.color)
print('Police type of my Car:', my_car.is_police)
