from datetime import datetime


def get_datetime(date):
    """Формат представления времени для сортировки"""
    thedate = datetime.fromisoformat(date)
    return thedate


def get_strftime(date):
    """Формат отображения даты для вывода дата.месяц.год"""
    thedate = datetime.fromisoformat(date)
    date_thedate = thedate.strftime("%d.%m.%Y")
    return date_thedate


def get_from(from_card):
    """Формат отображения номера карты ("MasterCard 6783 91** **** 1847") /
    счета "Счет **2662" """
    lst_from = from_card.split(" ")
    if len(lst_from) == 2:
        card_number = lst_from[1]
        name_card = lst_from[0]
    elif len(lst_from) == 3:
        card_number = lst_from[2]
        name_card = lst_from[0] + ' ' + lst_from[1]

    if lst_from[0] != "Счет":
        str_namber = ''
        i = 0
        for number in card_number:
            if i < 4:
                str_namber += number
                i += 1
            else:
                str_namber += ' '
                str_namber += number
                i = 1
            continue

        card_namber_disguised = str_namber.replace(str_namber[7:14], '** ****')
        return f'{name_card} {card_namber_disguised}'
    elif lst_from[0] == "Счет":
        account_number = card_number[-4:]
        return f"{name_card} **{account_number}"





