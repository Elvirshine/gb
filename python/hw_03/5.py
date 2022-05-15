print("Задание №5")

res = 0
garbage = False

while True:
    list_1 = list(map(str, input('Введите некоторое количество целых чисел через пробел: ').split()))

    for i in list_1:
        if i.isdigit():
            res += int(i)
        else:
            garbage = True
            break

    print(res)

    if garbage:
        break
