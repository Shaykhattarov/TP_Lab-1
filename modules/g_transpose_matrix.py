import numpy as np


def transpose_matrix():
    n, m = map(int, input().split())
    mas = []

    for k in range(n):
        mas.append([int(el) for el in input().split()])
    arr = np.array(mas)
    trans = arr.transpose()
    return trans


