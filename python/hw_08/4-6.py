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
