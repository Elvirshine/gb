print("Задание №2")

from abc import ABC


class Clothes(ABC):
    def __init__(self, height=1, volume=1):
        self.h = height
        self.v = volume

    @property
    def cons(self):
        return f"Сумарный расход ткани: {round(((2 * self.h + 0.3) + (self.v / 6.5 + 0.5)), 2)} "


class Coat(Clothes):
    def cons(self):
        return f"Для пошива пальто нужно {round((self.v / 6.5 + 0.5), 2)} м ткани"


class Costume(Clothes):
    def cons(self):
        return f"Для пошива костюма нужно {round((2 * self.h + 0.3), 2)} м ткани"


ct = Coat(400)
cs = Costume(55)
cl = Clothes(55, 400)
print(ct.cons())
print(cs.cons())
print(cl.cons)
