# Разработайте классы Circle, Rectangle, и Square.
# Каждый класс должен иметь метод для вычисления площади фигуры.

class Circule:
    def __init__(self, r):
        self.radius = r

    def finding_area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def finding_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def finding_area(self):
        return self.a ** 2

circle =Circule(5)
print(circle.finding_area())
rect = Rectangle(2, 5)
print(rect.finding_area())
square = Square(10)
print(square.finding_area())