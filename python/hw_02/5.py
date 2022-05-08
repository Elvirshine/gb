print("Задание №5")

my_list = [7, 5, 3, 3, 2]

print (f"Рейтинг: {my_list}")

new_el = int(input("Введите новый элемент рейтинга "))
my_list.append(new_el)
my_list.sort()
my_list.reverse()
print(my_list)
