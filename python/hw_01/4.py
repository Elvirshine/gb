# Задание 4
n = abs(int(input("Введите целое положительное число ")))
max_count = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_count:
        max_count = n % 10
    if n > 9:
        continue
    else:
        print("Максимальная цифра в числе ", max_count)
        break
