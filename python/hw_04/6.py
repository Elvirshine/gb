print("Задание №6a")
from itertools import count, cycle

x = abs(int(input('Введите действительное положительное число для старта цикла: ')))
y = abs(int(input('Введите действительное положительное число для завершения цикла: ')))

start = [el for el in range(x, (y+1))]  # без count
print(start)


for el in count(x):  # с count
    if el > y:
        break
    else:
        print(el)

print("Задание №6б")

с = 0
for el in cycle(["Abc", 123, "456"]):
    if с > y:
        break
    print(el)
    с += 1
