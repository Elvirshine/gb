print("Задание №1")

with open(r'file.txt', 'a') as file:
    while True:
        my_input = input('Введите данные на латинице:\n')
        if not my_input:
            break
        file.write(my_input + '\n')


my_file = open("file.txt", "r")
content = my_file.read()
print(content)
my_file.close()
