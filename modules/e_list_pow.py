import re


def list_pow_5():
    result = ""
    for num in [i for i in re.split(" |2|3|4|6|7|8", input()) if i != ""]:
        result = result + str(int(num) ** 2) + " "
    return result
