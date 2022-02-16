class Summator:

    def transform(self, n):
        return n

    def realise_sum(self, N):
        res = 0
        for n in range(1, N + 1):
            res += self.transform(n)
        return res


class PowerSummator(Summator):

    def __init__(self, b):
        self.b = b

    def transform(self, n):
        n = n ** self.b
        return n


class SquareSummator(PowerSummator):

    def __init__(self):
        self.b = 2


class CubeSummator(PowerSummator):

    def __init__(self):
        self.b = 3





def main():
    print("Введите последний элемент последовательности: ", end=" ")
    k = int(input())
    print("Введите степень в которую возводяться элементы последовательности: ", end=" ")
    b = int(input())

    power = PowerSummator(b)
    square = SquareSummator()
    cube = CubeSummator()

    res_sqr = square.realise_sum(k)
    res_cube = cube.realise_sum(k)
    res_power = power.realise_sum(k)
    res = ["Результат квадратного сумматора: " + str(res_sqr), "Результат кубического сумматора: " + str(res_cube), "Результат PowerSummator: " + str(res_power)]

    return res
