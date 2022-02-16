def encrypt_cesar_1():
    step = int(input())
    txt = str(input())
    result_txt = ""
    for char in txt:
        pos = ord(char)
        delta = pos + step

        if (pos >= 1040) and (pos <= 1071):
            if delta <= 1071:
                result_char = chr(delta)
                result_txt += result_char
            else:
                dif = delta - 1071
                result_char = chr(1040 + dif)
                result_txt += result_char
        elif (pos >= 1072) and (pos <= 1103):
            if delta <= 1103:
                result_char = chr(delta)
                result_txt += result_char
            else:
                dif = delta - 1103
                result_char = chr(1072 + dif)
                result_txt += result_char
        else:
            result_txt += char
    return result_txt
