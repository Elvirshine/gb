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
