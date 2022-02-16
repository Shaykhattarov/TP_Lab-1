def happy_birthday():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input().split(" "))

    m = int(input())
    req = []
    for i in range(m):
        req.append(input())

    result = []
    for i in range(n):
        if data[i][2] in req:
            result.append(data[i][0] + " " + data[i][1])

    result.sort()
    result.reverse()
    result_str = ""
    for res in result:
        result_str = result_str + res + "\n"
    return result_str
