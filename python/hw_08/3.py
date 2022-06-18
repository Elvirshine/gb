print("Задание №3")


class OwnError(Exception):
    def __init__(self, my_list):
        self.my_list = my_list


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise OwnError(value)
        my_list.append(int(value))
    except OwnError as ex:
        print('Вы ввели не число', ex)
print(my_list)
