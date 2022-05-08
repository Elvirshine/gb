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