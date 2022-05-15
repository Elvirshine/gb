print("Задание №4")
print("Вариант №1")
x = abs(int(input('Введите действительное положительное число: ')))
y = int(input('Введите целое полжительное число: '))


def my_func(x, y):
    x_st_y = x ** (y * (-1))
    return x_st_y


print(f'{x} в степени -{y} равняется {my_func(x, y)}')

