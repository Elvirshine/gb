print("Задание №4")

num_dict = {"One": "Один",
            "Two": "Два",
            "Three": "Три",
            "Four": "Четыре"
            }


def readEng():
    with open("numbers.txt", encoding="UTF-8") as numbers:
        return numbers.readlines()


def writeRus(lines):
    for line in lines:
        key = line.split(" ")[0]
        value = num_dict[key]
        line = line.replace(key, value)

        with open("rus_num.txt", "a", encoding="utf-8") as rus:
            print(line, file=rus)


lines = readEng()
writeRus(lines)