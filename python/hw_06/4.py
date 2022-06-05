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
