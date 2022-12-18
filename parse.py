



def check_line(input):
    text = input.replace(' ', '')
    if (not text[0].isdigit() and text[0] not in ['+','-','(']):
        return
    else:
        for i in range(len(text)):
            if text[i].isdigit() or text[i] in ['+','-','*','/', '(',')']:
                if (text[i] in ['+','-','*','/'] and i!=0):
                    if (text[i-1] in ['+','-','*','/']) or (text[i+1] in ['+','-','*','/']):
                        break
                elif text[i]=='(':
                    if not ')' in text[i+1:]:
                        break
            else:
                break
        else:
            return parse_line(text)


def parse_line(text):
    symbols = []
    i = 0
    while i in range(len(text)):
        if text[i].isdigit():
            num = text[i]
            if i + 1 == len(text):
                symbols.append(int(num))
                break
            while (text[i + 1].isdigit()):
                num = num + text[i + 1]
                i += 1
                if i + 1 == len(text):
                    break
            symbols.append(int(num))
            i += 1
        else:
            symbols.append(text[i])
            i += 1
    return symbols
