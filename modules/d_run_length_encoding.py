def run_length_encoding_4():
    sequence = str(input())
    ind = 1
    elem = sequence[0]
    count = 1
    while ind != len(sequence):
        if elem == sequence[ind]:
            count += 1
        else:
            print(str(count) + " " + elem)
            elem = sequence[ind]
            count = 1
        ind += 1
    return str(count) + " " + elem
