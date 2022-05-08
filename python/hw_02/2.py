print("Задание №2")

list_1 = list(map(int, input('Введите некоторое количество целых чисел через пробел: ').split()))

for i in range(0, len(list_1)-1, 2):
    list_1[i], list_1[i+1] = list_1[i+1], list_1[i]

print(list_1)
