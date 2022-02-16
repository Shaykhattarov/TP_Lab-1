class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Point):
            return self.x != other.x and self.y != other.y
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Point):
            return self.x + other.x,  self.y + other.y
        elif isinstance(other, int):
            return self.x + other, self.y + other
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return self.x - other.x,  self.y - other.y
        elif isinstance(other, int):
            return self.x - other, self.y - other
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x = self.x + other.x
            self.y = self.y + other.y
            return self.x, self.y
        elif isinstance(other, int):
            self.x = self.x + other
            self.y = self.y + other
            return self.x,  self.y
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Point):
            self.x = self.x - other.x
            self.y = self.y - other.y
            return self.x , self.y
        elif isinstance(other, int):
            self.x = self.x - other
            self.y = self.y - other
            return self.x, self.y
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int):
            return self.x * other, self.y * other
        else:
            return NotImplemented

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)


def main():
    print("Введите координаты 1-ой точки:", end=" ")
    x1, y1 = map(int, input().split())
    print("Введите координаты 2-ой точки:", end=" ")
    x2, y2 = map(int, input().split())
    print("Взайимодействующее с экземплярами число:", end=" ")
    k = int(input())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    result = []

    if p1 == p2:
        result.append("Equal True")
    else:
        result.append("Equal False")

    if p1 != p2:
        result.append("Not equal True")
    else:
        result.append("Not equal False")

    result.append("Результат выполнения сложения экземпляра и числа: " + str(p1 + k))
    result.append("Результат выполнения сложения двух экземпляров: " + str(p1 + p2))
    result.append("Результат выполнения вычитания экземпляра и числа: " + str(p1 - k))
    result.append("Результат выполнения вычитания двух экземпляров: " + str(p1 - p2))

    p1 += p2
    result.append("Результат выполнения сложения с присваиванием двух экземпляров: " + str(p1))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p1 -= p2
    result.append("Результат выполнения вычитания с присваиванием двух экземпляров: " + str(p1))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p1 += 3
    result.append("Результат выполнения сложения с присваиванием числа и экземпляра: " + str(p1))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p1 -= 3
    result.append("Результат выполнения вычитания с присваиванием числа и экземпляра: " + str(p1))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    result.append("Результат выполнения умножения двух экземпляров: " + str(p1 * p2))
    result.append("Результат выполнения умножения числа на экземпляр: " + str(p1 * k))

    result.append("Результат выполнения функции abs: " + str(abs(p1)))
    result.append("Результат выполнения функции len: " + str(len(p1)))

    return result

