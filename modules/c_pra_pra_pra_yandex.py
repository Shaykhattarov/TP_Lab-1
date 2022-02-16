def pra_pra_pra_yandex_3():
    data = []
    count_data = int(input())
    for i in range(count_data):
        data.append(str(input()))

    keys = []
    count_keys = int(input())
    for i in range(count_keys):
        keys.append(str(input()))

    res = []
    result = []
    for i in range(count_data):
        for j in range(count_keys):
            res.append(data[i].find(keys[j]))
        if -1 not in res:
            result.append(data[i])
        res.clear()

    result_str = ""
    for sentence in result:
        result_str = result_str + sentence + "\n"
    return result_str
