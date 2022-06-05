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
