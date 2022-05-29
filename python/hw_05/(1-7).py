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

print("Задание №3")


def staff_stat():
    try:
        with open("staff.txt", "r", encoding="utf-8") as staff:
            staff_list = staff.readlines()
            low_staff = []
            salaries = []
            for staff in staff_list:
                fam, money = staff.split(" ")
                salaries.append(float(money))
                if float(money) < 20000:
                    low_staff.append(fam)

        print(f"Сотрудники, имеющие оклад менее 20 тыс. рублей: {', '.join(low_staff)}\n"
              f"Средняя величина дохода сотрудников: {round(sum(salaries) / len(salaries), 2)}")
    except FileNotFoundError:
        return 'Файл не найден.'


staff_stat()

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

print("Задание №6")
import re
dictionary = {}

with open("lessons.txt", "r", encoding="utf-8") as lessons:
    lines = lessons.readlines()
    for line in lines:
        key, value = line.split(":")
        valueSum = 0

        for v in value.split(" "):
            item = re.sub(r'\D', "", v)
            if item.isdigit():
                valueSum += int(item)

        dictionary[key] = valueSum

print(dictionary)

print("Задание №7")

dictAll = {}
dictAverage = {}
result = [dictAll, dictAverage]

with open("company.txt", "r", encoding="utf-8") as company:
    comp_list = company.readlines()
    positive = []
    negative = []
    for company in comp_list:
        firm, own, profit, costs = company.split(" ")
        margin = float(profit) - float(costs)
        if margin < 0:
            negative.append(float(margin))
        else:
            positive.append(float(margin))
        dictAll[firm] = margin

    dictAverage["average_profit"] = round(sum(positive) / len(positive), 2)

print(result)
