print("Задание №4")

words = list(input("Введите слова через пробел ").split())
for ind, el in enumerate(words, 1):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind, el[0:10])