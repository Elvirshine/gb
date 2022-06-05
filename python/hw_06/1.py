print("Задание 1")
from itertools import cycle
from time import sleep


class TrafficLight:

    # метод
    def running(__color = ["Красный", "Желтый", "Зеленый"]):
        for i, col in enumerate(cycle(__color)):
            print(col)
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                break


traffic = TrafficLight
traffic.running()
