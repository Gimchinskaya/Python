import time


class TrafficLight:
    def __init__(self):
        self._color = "red"

    def running(self):
        print(self._color)
        time.sleep(7)
        self._color = "yellow"
        print(self._color)
        time.sleep(2)
        self._color = "green"
        print(self._color)
        time.sleep(5)
        print('The traffic light is finished')


my_trafficlight = TrafficLight()
my_trafficlight.running()

