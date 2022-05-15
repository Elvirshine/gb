print("Задание №6")

import re

string = input('Введите слово латинскими прописными буквами: ')


def int_func(str):
    return str.title()


if not len(re.findall(r"[^a-z\s]", string)):
    print(int_func(string))