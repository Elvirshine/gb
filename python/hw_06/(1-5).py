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

print("Задание 2")


class Road:

    def __init__(self, length, width):
        self._length = length  # длина
        self._width = width  # ширина
        self.weight = 25  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
        self.depth = 5  # толщина полотна  #     _length*_width*weight*depth = массы асфальта, необходимого для покрытия всего дорожного полотна.

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.depth
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {asphalt_mass} кг или {round(asphalt_mass / 1000)} т')


r = Road(5000, 20)
r.asphalt_mass()

print("Задание 3")


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Антон', 'Чехов', 'писатель', '200000', '30000')
print(f"Полное имя: {p.get_full_name()}\nЗарплата: {p.get_total_income()}")

print("Задание 4")


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} приехала")

    def turn_direction(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"со скоростью {self.speed} км/ч")


class TownCar(Car):
    def speed_reduction(self):
        if self.speed > 60:
            print(f"{self.name} превысилa скорость в зоне города на {self.speed - 60} км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def speed_reduction(self):
        if self.speed > 40:
            print(f"{self.name} превысилa скорость в промышленной зоне на {self.speed - 40} км/ч")


class PoliceCar(Car):
    pass


# c = Car(100, 'red', 'audi', False)
t = TownCar(67, 'blue', 'bmw', True)
w = WorkCar(50, 'white', 'citroen', False)
s = SportCar(120, 'green', 'bugatti', True)
p = PoliceCar(150, 'black', 'ford', True)
t.go(), t.show_speed(), t.speed_reduction(), t.turn_direction("налево"), t.turn_direction("направо"), t.stop()
print(f'\n'), s.go(), s.show_speed(), s.turn_direction('налево'), s.stop()
print(f'\n'), w.go(), w.show_speed(), w.speed_reduction(), w.turn_direction('направо'), w.stop()
print(f'\n'), p.go(), p.show_speed(), p.turn_direction('направо'), p.stop()

print("Задание 5")


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return f"Рисовать {self.title} ручкой"


class Pencil(Stationery):
    def draw(self):
        return f"Рисовать {self.title} карандашом"


class Handle(Stationery):
    def draw(self):
        return f"Рисовать {self.title} маркером"


s = Stationery('title')
p = Pen('title')
pc = Pencil('title')
h = Handle('title')
print(s.draw())
print(p.draw())
print(pc.draw())
print(h.draw())
