import json


def get_five_operation(operations):
    """
    получает 5 операций и переворачивает их
    """
    with open(operations,  encoding='utf-8') as f:
        list_operations = json.load(f)

        def sort_(e):
            if e == {}:
                return tuple(map(int, [2019, 8, 26]))
            else:
                return tuple(map(int, (e['date'].split('T'))[0].split('-')))

        sorted_date = sorted(list_operations, key=sort_)
        five_last_operations = sorted_date[-5:]
        five_last_operations.reverse()
        return five_last_operations


def grouper_card(num):
    """
    переводит номер карты в формат - по условию
    """
    list_ = []
    for i in range(0, 16):
        if i < 6 or i > 11:
            list_.append(num[i])
            if i == 3:
                list_.append(' ')
        else:
            list_.append('*')
            if i == 7 or i == 11:
                list_.append(' ')
    return ''.join(list_)


def grouper_account(num):
    """
    переводит номер счёта в формат - по условию
    """
    list_ = []
    for i in range(0, 20):
        if 16 > i > 13:
            list_.append('*')
        elif i > 15:
            list_.append(num[i])
    return ''.join(list_)


def get_date_revers(operation):
    """
    получает и переворачивает дату
    """
    date_ = (operation['date'].split('T'))[0].split('-')
    date_.reverse()
    return '.'.join(date_)


def get_from_and_to(operation):
    """
    собирает все данные вместе и возвращает их
    """
    to_num = operation['to'].split()[-1]
    if len(to_num) == 20:
        to_num_hide = grouper_account(to_num)
    else:
        to_num_hide = grouper_card(to_num)
    to_name = ' '.join(operation['to'].split()[:-1])
    if len(operation) > 6:
        from_num = operation['from'].split()[-1]
        if len(from_num) == 20:
            from_num_hide = grouper_account(from_num)
        else:
            from_num_hide = grouper_card(from_num)
        from_name = ' '.join(operation['from'].split()[:-1])
        return [from_name, from_num_hide, to_num_hide, to_name]
    return [0, 0, to_num_hide, to_name]


