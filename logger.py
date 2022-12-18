from datetime import datetime as dt


def signs_logger(num):
    time=dt.now().strftime('%H:%M')
    with open('log.csv','a', encoding='UTF-8') as file:
        file.write('{};sign;{}\n'
                    .format(time, num))

def arguments_logger(num):
    time=dt.now().strftime('%H:%M')
    with open('log.csv','a', encoding='UTF-8') as file:
        file.write('{};argument;{}\n'
                    .format(time, num))

def results_logger(num):
    time=dt.now().strftime('%H:%M')
    with open('log.csv','a', encoding='UTF-8') as file:
        file.write('{};result;{}\n'
                    .format(time, num))

