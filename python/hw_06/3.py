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
