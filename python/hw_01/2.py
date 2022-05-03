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
