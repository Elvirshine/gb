print("Задание №4")

from collections import Counter


start = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
s = Counter(start)
result = [key for key in s if s[key] < 2]

print(f"Исходный список: {start}")
print(f"Результат: {result}")

