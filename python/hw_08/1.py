print("Задание №1")


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    @staticmethod
    def date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))

        if (32 > day > 0) and (12 > month > 0) and (year < 5000):
            print(date_str)
            return day, month, year
        else:
            print('Ошибка ввода данных')


Date.date_valid('13-11-2002')
Date.date_valid('34-11-2002')
Date.date_valid('13-13-2002')
Date.date_valid('13-11-5002')
