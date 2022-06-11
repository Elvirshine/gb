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
