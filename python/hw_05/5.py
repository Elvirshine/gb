print("Задание №5")

with open(r'Numset.txt', 'a', encoding="utf-8") as file:
    while True:
        my_input = input('Введите целое число (двойной Enter заканчивает ввод чисел):\n')
        if not my_input:
            break
        file.write(my_input + ' ')


with open(r'Numset.txt', 'r', encoding="utf-8") as newfile:
    my_list = newfile.readline().split(" ")
    sum = 0
    for n in my_list:
        if n.isdigit():
            sum += int(n)
    print(f"Сумма введеных чисел: {sum}")

