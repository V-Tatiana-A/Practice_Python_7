
import view
import model
import parse
import logger as log

def input_first():
    number=view.input_argument()
    model.set_first(number)
    log.arguments_logger(number)

def input_second():
    while True:
        number = view.input_argument()
        if model.get_operation()=='/' and number==0:
            view.print_devision_by_zero()
        else:
            model.set_second(number)
            log.arguments_logger(number)
            break

def input_operation():
    oper=view.input_operation()
    model.set_operation(oper)
    log.signs_logger(oper)


def solution():
    if isinstance(model.get_first(), list):
        model.expression(model.get_first())
        model.set_first(model.get_result())
    if isinstance(model.get_second(), list):
        model.expression(model.get_second())
        model.set_second(model.get_result())
    oper=model.get_operation()
    match oper:
        case '+':
            model.addition()
        case '-':
            model.difference()
        case '*':
            model.multiplication()
        case '/':
            model.division()

    resul_string=f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'

    view.print_to_console(resul_string)
    model.set_first(model.get_result())
    log.results_logger(model.get_result())

def start():
    input_first()
    while True:
        input_operation()
        if model.get_operation() =='=':
            if isinstance(model.get_first(), list):
                model.expression(model.get_first())
            view.log_off(model.get_result())
            log.results_logger(model.get_result())
            break
        input_second()
        solution()




