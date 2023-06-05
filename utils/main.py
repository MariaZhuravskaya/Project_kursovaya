import json
from functions import get_datetime, get_strftime, get_from

with open("operations.json", encoding="UTF-8") as operations:
    operation = json.load(operations)

# список значений по ключу d["date"]
lst_date = []
for d in operation:
    if d != {}:
        date = d["date"]
        lst_date.append(date)

# список дат транзакций и сортировка по убыванию
lst_datetime = []
for i in lst_date:
    lst_datetime.append(get_datetime(i))

sorted_lst_datetime = sorted(lst_datetime, reverse=True)


# Выбор последнич 5 выполненных (EXECUTED) операций
application = []
i = 0
for date in sorted_lst_datetime:
    if i != 5:
        for d in operation:
            if d != {} and get_datetime(d["date"]) == date:
                if d["state"] == "EXECUTED":
                    application.append(d)
                    i += 1


for d in application:
    if d != {}:
        if "from" in d:
            print(f"""{get_strftime(d["date"])} {d["description"]}
{get_from(d["from"])} -> {get_from(d["to"])}
{d["operationAmount"]["amount"]} {d["operationAmount"]["currency"]["name"]}
""")
        else:
            print(f"""{get_strftime(d["date"])} {d["description"]}
{get_from(d["to"])}
{d["operationAmount"]["amount"]} {d["operationAmount"]["currency"]["name"]}
""")