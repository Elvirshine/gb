print("Задание №7")
from math import factorial

y = abs(int(input('Введите действительное положительное число для завершения цикла: ')))


def fact(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)


for el in fact(y):
    print(el)
