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
