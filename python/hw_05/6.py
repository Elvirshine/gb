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