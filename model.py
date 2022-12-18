
first_number=0
second_number=0
operation=''
result=0



def get_first():
    global first_number
    return first_number

def get_second():
    global second_number
    return second_number

def get_operation():
    global operation
    return operation

def get_result():
    global result
    return result





def set_first(value):
    global first_number
    first_number=value

def set_second(value):
    global second_number
    second_number=value

def set_operation(value):
    global operation
    operation=value

def addition():
    global first_number
    global second_number
    global result
    result=first_number+second_number

def difference():
    global first_number
    global second_number
    global result
    result=first_number-second_number

def multiplication():
    global first_number
    global second_number
    global result
    if isinstance(first_number, float):
        if first_number==int(first_number):
            first_number = int(first_number)
        else:
            second_number=float(second_number)
    elif isinstance(second_number, float):
        if second_number==int(second_number):
            second_number=int(second_number)
        else:
            first_number=float(first_number)
    result=first_number*second_number
    if result==int(result):
        result=int(result)

def division():
    global first_number
    global second_number
    global result
    result=first_number/second_number
    if result==int(result):
        result=int(result)


def expression(exp):
    global result
    list=exp
    while len(list) != 1:
        i = 0
        while ')' in list and i < len(list):
            open = list.index('(')
            close = list.index(')')
            for j in range(open, close):
                while '*' in list[open:close] or '/' in list[open:close]:
                    if list[j] == '*':
                        result = list[j - 1] * list[j + 1]
                        list.pop(j)
                        list.pop(j)
                        list[j - 1] = result
                        j -= 1
                    elif list[j] == '/':
                        result = list[j - 1] / list[j + 1]
                        list.pop(j)
                        list.pop(j)
                        list[j - 1] = result
                        j -= 1
                    j += 1
                    if list.index('(') == list.index(')') - 2:
                        list.pop(j)
                        list.pop(j - 2)

                while '+' in list[open:close] or '-' in list[open:close]:
                    if list[j] == '+':
                        result = list[j - 1] + list[j + 1]
                        list.pop(j)
                        list.pop(j)
                        list[j - 1] = result
                        j -= 1
                    elif list[j] == '-':
                        result = list[j - 1] - list[j + 1]
                        list.pop(j)
                        list.pop(j)
                        list[j - 1] = result
                        j -= 1
                    j += 1
                    if list.index('(') == list.index(')') - 2:
                        list.pop(j)
                        list.pop(j - 2)
                        break
                break

        while ('*' in list or '/' in list) and i < len(list):
            if list[i] == '*':
                result = list[i - 1] * list[i + 1]
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i -= 1
            elif list[i] == '/':
                result = list[i - 1] / list[i + 1]
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i -= 1
            i += 1

        i = 0
        while ('+' in list or '-' in list) and i < len(list):
            if list[i] == '+' and i != 0:
                result = list[i - 1] + list[i + 1]
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i += 1
            elif list[i] == '-' and i != 0:
                result = list[i - 1] - list[i + 1]
                list.pop(i)
                list.pop(i)
                list[i - 1] = result
                i += 1
            elif list[i] == '-' and i == 0:
                list[i + 1]=-list[i + 1]
                list.pop(i)
            i += 1
    if result==int(result):
        result=int(result)