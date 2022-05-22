print("Задание №1")

from sys import argv

script_name, hours, rate, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", hours)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print("Итого: ", (float(hours) * float(rate)) + float(bonus))

print("Задание №2")

start = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [current for current in start if start.index(current) > 0 and (current > start[start.index(current)-1])]
# start.index(current) - индекс предыдущего числа

print(f"Исходный список: {start}")
print(f"Результат: {result}")

print("Задание №3")

list = [el for el in range(20,241) if (el % 20 == 0) or (el % 21 == 0)]
print(list)

print("Задание №4")

from collections import Counter


start = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
s = Counter(start)
result = [key for key in s if s[key] < 2]

print(f"Исходный список: {start}")
print(f"Результат: {result}")

print("Задание №5")

from functools import reduce

start = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(lambda x, y: x * y, start))
print(start)


print("Задание №6a")
from itertools import count, cycle

x = abs(int(input('Введите действительное положительное число для старта цикла: ')))
y = abs(int(input('Введите действительное положительное число для завершения цикла: ')))

start = [el for el in range(x, (y+1))]  # без count
print(start)


for el in count(x):  # с count
    if el > y:
        break
    else:
        print(el)

print("Задание №6б")

с = 0
for el in cycle(["Abc", 123, "456"]):
    if с > y:
        break
    print(el)
    с += 1

    print("Задание №7")
    from math import factorial

    y = abs(int(input('Введите действительное положительное число для завершения цикла: ')))


    def fact(n):
        for i in range(n):
            print(i, end='! = ')
            yield factorial(i)


    for el in fact(y):
        print(el)

