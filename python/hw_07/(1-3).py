print("Задание №1")


class Matrix:
    def __init__(self, my_array):
        self.my_array = my_array

    def __str__(self):
        result = ''
        for a in self.my_array:
            result += f"{' '.join(str(v) for v in a)}\n"
        return result

    def __add__(self, other):
        for i in range(len(self.my_array)):
            for j in range(len(self.my_array[i])):
                self.my_array[i][j] += other.my_array[i][j]
        return self


m = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
p = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(m)
print(p)
print(m + p)


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


print("Задание №3")


class Cell:
    def __init__(self, quantity=int):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self):
        return f"{self.quantity}"

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


c_1 = Cell(15)
c_2 = Cell(4)
print(f"Сложение: {c_1 + c_2}\nВычитание: {c_1 - c_2}\nУмножение: {c_1 * c_2}\nДеление: {c_1 / c_2}")
print(c_1.make_order(6))
