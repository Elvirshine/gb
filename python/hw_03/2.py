print("Задание №2")


name = input('Введите имя ')
lastname = input('Введите фамилию ')
birth_year = input('Введите год рождения ')
city = input('Введите город проживания ')
email = input('Введите email ')
phone = input('Введите номер телефона ')


def second_func(fname=name, lname=lastname, birth=birth_year, lcity=city, mail=email, tphone=phone):
    return fname, lname, birth, lcity, mail, tphone

print(second_func())
