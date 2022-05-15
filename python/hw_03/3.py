print("Задание №3")

n = list(map(int, input('Введите три целых числа через пробел: ').split()))


def my_func(c_1, c_2, c_3):
    c = [c_1, c_2, c_3]
    c.remove(min(c))
    return (sum(c))


print(my_func(n[0], n[1], n[2]))
