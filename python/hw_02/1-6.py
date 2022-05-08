print("Задание №1")

int_ = 1
str_ = "rumba"
list_ = ["tango", 2]
tuple_ = ('chacha', '3')
dict_ = {'city': 'Moscow', 'country': 'Russia'}
none_ = None
bool_ = bool(4<5)
byte_ = b"quick step"
set_ = {6, 7, 8}

print(
      type(int_), type(str_), type(list_),
      type(tuple_), type(dict_), type(none_),
      type(bool_), type(byte_), type(set_)
    )

print("Задание №2")

list_1 = list(map(int, input('Введите некоторое количество целых чисел через пробел: ').split()))

for i in range(0, len(list_1)-1, 2):
    list_1[i], list_1[i+1] = list_1[i+1], list_1[i]

print(list_1)

print("Задание №3")

num = int(input("Введите номер месяца "))
print("Список: ")
quart_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]

if num in range(1, 13):
    for i, el in enumerate(quart_list):
        if num in el[1:4]:
            print(el[0])
            break
else:
    print("Ошибка!")

print("Словарь: ")
quart_dict = {"Зима": (1, 2, 12),
           "Весна": (3, 4, 5),
           "Лето": (6, 7, 8),
           "Осень": (9, 10, 11)}

for key in quart_dict.keys():
    if num in quart_dict[key]:
        print(key)

print("Задание №4")

words = list(input("Введите слова через пробел ").split())
for ind, el in enumerate(words, 1):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind, el[0:10])

print("Задание №5")

my_list = [7, 5, 3, 3, 2]

print (f"Рейтинг: {my_list}")

new_el = int(input("Введите новый элемент рейтинга "))
my_list.append(new_el)
my_list.sort()
my_list.reverse()
print(my_list)

print("Задание №6")

goods = []
number = 0

print('Введите одной строкой название товара, цену, количество и единицу измерения')
print('В качестве разделителя позиций используйте только один символ запятой')
print('Значения цены и количества должны быть целочисленными')
print('Для завершения введите пустую строку')

while True:
    number += 1
    good_list = input(f'{number} товар: ').split(',')
    if good_list == ['']:
        break

    goods.append((number, {'Наименование': good_list[0],
                           'Цена': int(good_list[1]),
                           'Количество': int(good_list[2]),
                           'Ед. изм.': good_list[3]}))

goods_dict = {}

for i, el in enumerate(list(goods[0][1].keys())):
    goods_dict[el] = []

for i, el in enumerate(goods_dict):
    dict_list = []

    for j, el_goods in enumerate(goods):
        key_val = el_goods[1].get(el)

        if key_val not in dict_list:
            dict_list.append(key_val)

    goods_dict[el] = dict_list

print(goods_dict)

