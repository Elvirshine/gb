print("Задание №7")


class Complex_num:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.math_ex = (num_1 + num_2) / num_2

    def pprint(self):
        # return f"{self.num_1}, {self.num_2}"
        return f'({self.num_1}+{self.num_2})/{self.num_2}'

    def __add__(self, other):
        return Complex_num(self.num_1 + other.num_1, self.num_2 + other.num_2)

    def __mul__(self, other):
        return Complex_num(self.num_1 * other.num_1, self.num_2 * other.num_2)

    def __str__(self):
        return f"{self.math_ex}"


c_1 = Complex_num(100, 2)
c_2 = Complex_num(10, 5)
c_1.pprint()
c_2.pprint()
print(f"Выражения: {c_1.pprint()}, {c_2.pprint()}\nСложение выражений: {c_1 + c_2}\nУмножение выражений: {c_1 * c_2}")
