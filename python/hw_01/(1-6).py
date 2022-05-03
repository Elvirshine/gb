# Задание №1
name = "Максим"
lastname = "Горький"
print(f"Меня зовут {name} {lastname}")

name = input("Введите имя ")
age = int(input("Введите год рождения "))
place = input("Введите место рождения ")

print(f"Меня зовут {name}. Я родился: {age}г., {place}")

# Задание №2
time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - 3600) // 60
seconds = 3765 % 3600 % 60

if hours <= 9:
    hours = "0"+str(hours)

if minutes <= 9:
    minutes = "0"+str(minutes)

if seconds < 10:
    seconds = "0"+str(seconds)

print(f"{hours}:{minutes}:{seconds}")

# Задание 3 (3 варианта решения задачи)
#1
n = int(input("Введите число "))
nn = n * 11
nnn = n * 111
total = n + nn + nnn

print(f"{n}+{nn}+{nnn}={total}")
#2
print(f"{n}+{n*11}+{n*111}={n+n*11+n*111}")
#3
nn = int(str(n)+str(n))
nnn = int(str(nn)+str(n))
print(f"{n}+{nn}+{nnn}={n+nn+nnn}")

# Задание 4
n = abs(int(input("Введите целое положительное число ")))
max_count = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_count:
        max_count = n % 10
    if n > 9:
        continue
    else:
        print("Максимальная цифра в числе ", max_count)
        break

# Задание 5
revenue = int(input("Введите сумму выручки "))
costs = int(input("Введите сумму издержек "))
if revenue > costs:
    profit = revenue-costs
    rent = profit/revenue
    print(f"Прибыль. Рентабельность равна {rent}")
    staff = int(input("Введите численность сотрудников "))
    profit_per_staff = profit/staff
    print(f"В расчете на одного сотрудника прибыль составила {profit_per_staff} рублей.")
else:
    print("Убыток")

# Задание 6
a = int(input("Введите расстояние, которое спортсмен пробежал в первый день "))
b = int(input("Введите расстояние, которое спортсмен  должен пробежать на определяемый день "))
days = 1
print(f"{days}-й день: {a}")
while a < b:
    a = round (a + a * 0.1, 2)
    days += 1
    if a <= b:
        print(f"{days}-й день: {a}")
    else:
        print(f"{days}-й день: {a}")
else:
    print(f"Ответ: на {days}-й день спортсмен достиг результата — не менее {b} км.")
