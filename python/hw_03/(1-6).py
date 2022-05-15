print("Задание №1")
print("Вариант №1")

arg_1 = abs(int(input("Введите целое положительное число: ")))  # Ввод данных в варианте №1
arg_2 = abs(int(input("Введите еще одно целое положительное число: ")))


def my_del(arg_1, arg_2):  # Функция, которая делит одно число на другое в варианте №1
    try:  # Обработка ситуации деления на ноль
        return arg_1 / arg_2
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

print(my_del(arg_1, arg_2))

print("Вариант №2")
n = list(map(int, input('Введите два целых числа через пробел: ').split()))  # Ввод данных в варианте №2

arg_1 = n[0]  # Присваивание переменных в варианте №2
arg_2 = n[1]


def my_del(arg_1, arg_2):  # Функция, которая делит одно число на другое в варианте №2
    try:  # Обработка ситуации деления на ноль
        return arg_1 / arg_2
    except ZeroDivisionError:
        return (f"На ноль делить нельзя!")


print(my_del(arg_1, arg_2))


print("Задание №2")


name = input('Введите имя ')
lastname = input('Введите фамилию ')
birth_year = input('Введите год рождения ')
city = input('Введите город проживания ')
email = input('Введите email ')
phone = input('Введите номер телефона ')


def second_func(fname=name, lname=lastname, birth=birth_year, lcity=city, mail=email, tphone=phone):
    return fname, lname, birth, lcity, mail, tphone

print(second_func())


print("Задание №3")

n = list(map(int, input('Введите три целых числа через пробел: ').split()))


def my_func(c_1, c_2, c_3):
    c = [c_1, c_2, c_3]
    c.reverse()
    print(c[0] + c[1])


my_func(n[0], n[1], n[2])


print("Задание №4")
print("Вариант №1")
x = abs(int(input('Введите действительное положительное число: ')))
y = int(input('Введите целое полжительное число: '))


def my_func(x, y):
    x_st_y = x ** (y * (-1))
    return x_st_y


print(f'{x} в степени -{y} равняется {my_func(x, y)}')


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


print("Задание №6")

import re

string = input('Введите слово латинскими прописными буквами: ')


def int_func(str):
    return str.title()


if not len(re.findall(r"[^a-z\s]", string)):
    print(int_func(string))