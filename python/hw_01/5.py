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

