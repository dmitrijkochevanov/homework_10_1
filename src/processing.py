def get_dictionary_key(list_dict: list, state: str ="EXECUTED") -> list:
    """Функция,которая фильтрует список словарей по ключу state"""
    filtred_list = []
    for ld in list_dict:
        if ld.get("state") == state:
            filtred_list.append(ld)
    return filtred_list


def get_date_sorted(list_dict: list, direction: bool = True) -> list:
    """Функция сортирует словари по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list

print(get_date_sorted([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

