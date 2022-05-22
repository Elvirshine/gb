print("Задание №1")

from sys import argv

script_name, hours, rate, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", hours)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print("Итого: ", (float(hours) * float(rate)) + float(bonus))

