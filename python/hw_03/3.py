print("Задание №3")

n = list(map(int, input('Введите три целых числа через пробел: ').split()))


def my_func(c_1, c_2, c_3):
    c = [c_1, c_2, c_3]
    c.reverse()
    print(c[0] + c[1])


my_func(n[0], n[1], n[2])

