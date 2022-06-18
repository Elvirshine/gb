print("Задание №2")

n = list(map(int, input('Введите два целых числа через пробел: ').split()))

divisible = n[0]
divisor = n[1]


class Zerodiv:
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor

    @staticmethod
    def zero(divisible, divisor):
        try:
            res = divisible / divisor
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        else:
            print(f"Все хорошо. Результат - {res}")
        finally:
            print("Программа завершена")


Zerodiv.zero(n[0], n[1])
