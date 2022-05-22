print("Задание №5")

from functools import reduce

start = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(lambda x, y: x * y, start))
print(start)

