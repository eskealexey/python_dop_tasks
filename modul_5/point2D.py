# Точка в 2D пространстве
# Создайте класс Point, который инициализируется с координатами x и y.
# Включите в класс метод для вычисления расстояния до другой точки.
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x1 = self.x - other.x
        y1 = self.y - other.y
        return 'Расстояние между точками равно {:.4f}'.format(math.sqrt(x1 ** 2 + y1 ** 2))


pnt1 = Point(0, 3)
pnt2 = Point(4, 0)
print(Point.distance(pnt1, pnt2))
