class Summator:

    def transform(self, n):
        pass

    def realise_sum(self, N):
        res = 0
        for n in range(1, N + 1):
            res += self.transform(n)
        return res


class SquareSummator(Summator):

    def transform(self, n):
        n = n ** 2
        return n


class CubeSummator(Summator):

    def transform(self, n):
        n = n ** 3
        return n


def main():
    k = int(input())
    square = SquareSummator()
    cube = CubeSummator()

    res_sqr = square.realise_sum(k)
    res_cube = cube.realise_sum(k)
    res = ["Результат квадратного сумматора: " + str(res_sqr), "Результат кубического сумматора: " + str(res_cube)]

    return res
