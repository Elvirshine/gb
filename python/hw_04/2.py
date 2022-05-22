print("Задание №2")

start = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [current for current in start if start.index(current) > 0 and (current > start[start.index(current)-1])]
# start.index(current) - индекс предыдущего числа

print(f"Исходный список: {start}")
print(f"Результат: {result}")
