# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
print("Задание №2")

my_file = open("file.txt", "r")
content = my_file.read()
print(content)
my_file.close()

count = 0
with open("file.txt") as f:
    for line in f:
        count += 1
print(f"Строк в файле: {count}")


def word_counter():
    with open("file.txt") as f:
        my_list = f.readlines()
        for word in range(len(my_list)):
            new_l = my_list[word].split()
            print(f'В {word + 1}-ой строке слов: {len(new_l)}')


word_counter()
