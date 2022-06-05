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
