print("Задание №1")


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    @staticmethod
    def date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))

        if (32 > day > 0) and (12 > month > 0) and (year < 5000):
            print(date_str)
            return day, month, year
        else:
            print('Ошибка ввода данных')


Date.date_valid('13-11-2002')
Date.date_valid('34-11-2002')
Date.date_valid('13-13-2002')
Date.date_valid('13-11-5002')

print("Задание №2")

n = list(map(int, input('Введите два целых числа через пробел: ').split()))

divisible = n[0]
divisor = n[1]


class Zerodiv:
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor

    @staticmethod
    def zero(divisible, divisor):
        try:
            res = divisible / divisor
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        else:
            print(f"Все хорошо. Результат - {res}")
        finally:
            print("Программа завершена")


Zerodiv.zero(n[0], n[1])

print("Задание №3")


class OwnError(Exception):
    def __init__(self, my_list):
        self.my_list = my_list


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise OwnError(value)
        my_list.append(int(value))
    except OwnError as ex:
        print('Вы ввели не число', ex)
print(my_list)

print("Задания №4-6")


class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f"Not enough space, current = {self.current}, needle = {self.needle}"


class Storage:
    capasity: int
    product_type: list

    def __init__(self, capacity=0):
        self.capacity = capacity
        self.product_type = []

    def store(self, product_type: list):
        if len(self.product_type) >= self.max_count:
            raise CapacityException(len(self.product_type), len(self.product_type) + len(product_type))
        elif len(product_type) > (self.max_count - len(self.product_type)):
            raise CapacityException(self.max_count, len(self.product_type) + len(product_type))

        self.product_type.extend(product_type)


class Equipment:
    name: str
    quantity: int
    price: float

    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price


class Printer(Equipment):
    print_formats = [1, 2, 3, 4, 5]
    print_format: str = None
    colored: bool = False

    def __init__(self, name, price, print_format, colored, quantity=1):
        super().__init__(name, price, quantity)
        self.print_format = print_format
        self.colored = colored

    def __str__(self):
        return '{name} {print_format} {colored} {price}руб' \
            .format(
            name=self.name,
            print_format=self.print_format,
            colored="colored" if self.colored else "monochrome",
            price=self.price)

    def pprint(self):
        return f'Название: {self.name}, формат: {self.print_format}, количество цветов: {self.colored}, цена: {self.price}руб, количество: {self.quantity}'


class Scaner(Equipment):
    scan_formats = [1, 2, 3, 4, 5]
    scan_format: str = None

    def __init__(self, name, price, scan_format, quantity=1):
        super().__init__(name, price, quantity)
        self.scan_format = scan_format

    def pprint(self):
        return f'Название: {self.name}, формат: {self.scan_format}, цена: {self.price}руб, количество: {self.quantity}'


class Xerox(Equipment):
    xerox_formats = [1, 2, 3, 4, 5]
    xerox_format: str = None

    def __init__(self, name, price, xerox_format, quantity=1):
        super().__init__(name, price, quantity)
        self.xerox_format = xerox_format

    def pprint(self):
        return f'Название: {self.name}, формат: {self.xerox_format}, цена: {self.price}руб, количество: {self.quantity}'


unit_1 = Printer('hp', 2000, 5, "monochrome")
unit_2 = Scaner('Canon', 1200, 3, 2)
unit_3 = Xerox('Xerox', 1500, 2, 15)
print(unit_1.pprint())
print(unit_2.pprint())
print(unit_3.pprint())

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
