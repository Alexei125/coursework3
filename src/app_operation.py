from utils import functions


def app_operation(operations):
    """
    получает 5 операций и выводит информацию по каждой в нужном формате
    """
    five_operations = functions.get_five_operation(operations)
    for operation in five_operations:
        date = functions.get_date_revers(operation)
        from_name, from_num_hide, to_num_hide, to_name = functions.get_from_and_to(operation)
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f'\n{date} {operation["description"]}')
        if from_name != 0:
            print(f'{from_name} {from_num_hide} -> {to_name} {to_num_hide}')
        else:
            print(f'{to_name} {to_num_hide}')
        print(f'{amount} {currency}')
