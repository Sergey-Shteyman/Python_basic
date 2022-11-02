import math


class Square:
    def __init__(self, a):
        self.figure_name = "Квадрат"
        self.a = a

    @property
    def square(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, h):
        self.figure_name = "Треугольник"
        self.a = a
        self.h = h

    @property
    def square(self):
        return 0.5 * self.a * self.h

    @property
    def perimeter(self):
        return 2 * math.sqrt(self.h**2 + (self.a / 2)**2) + self.a


class Cube(Square):
    def __init__(self, a):
        super().__init__(a)
        self.figure_name = 'Куб'

    @property
    def square(self):
        return 6 * super().square

    @property
    def perimeter(self):
        return 3 * super().perimeter


class Pyramid(Triangle, Square):
    def __init__(self, a, h):
        super().__init__(a, h)
        self.figure_name = 'Пирамида'

    @property
    def square(self):
        side_square = 4 * super().square
        base_square = self.a ** 2
        return side_square + base_square

    @property
    def perimeter(self):
        return 2 * super().perimeter + 2 * self.a


p = Pyramid(6, 4)
print(p.square)
print(p.perimeter)

p = Cube(5)
print(p.square)
print(p.perimeter)
