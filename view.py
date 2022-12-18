import parse


def error():
    print('Ошибка ввода')

def input_argument():
    while True:
        enter=input('Введите натуральное число или сразу выражение с натуральными числами: ')
        if enter.isdigit():
            return int(enter)
        else:
            if parse.check_line(enter):
                return parse.check_line(enter)
            else:
                error()



def input_operation():
    while True:
        operation=input('Введите операцию: ')
        if operation in ['+','-','*','/','=']:
            return operation
        else:
            print('Введите корректную операцию')

def print_to_console(value_text):
    print(value_text)

def log_off(res):
    print(f'Найденный результат равен {res}. До свидания!')

def print_devision_by_zero():
    print('На ноль делить нельзя')


