import math


class Square:
    def __init__(self, side):
        self.figure_name = "Квадрат"
        self.side = side

    @property
    def square(self):
        """Возвращает площадь квадрата"""
        return self.side ** 2

    @property
    def perimeter(self):
        """Возвращает периметр квадрата"""
        return 4 * self.side


class Triangle:
    def __init__(self, side, height):
        self.figure_name = "Треугольник"
        self.side = side
        self.height = height

    @property
    def square(self):
        """Возвращает площадь треугольника"""
        return 0.5 * self.side * self.height

    @property
    def perimeter(self):
        """Возвращает периметр треугольника"""
        return 2 * math.sqrt(self.height ** 2 + (self.side / 2) ** 2) + self.side


class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
        self.figure_name = 'Куб'

    @property
    def square(self):
        """Возвращает площадь куба"""
        return 6 * super().square

    @property
    def perimeter(self):
        """Возвращает периметр куба"""
        return 3 * super().perimeter


class Pyramid(Triangle, Square):
    def __init__(self, side, height):
        super().__init__(side, height)
        self.figure_name = 'Пирамида'

    @property
    def square(self):
        """Возвращает площадь пирамиды"""
        side_square = 4 * super().square
        base_square = self.side ** 2
        return side_square + base_square

    @property
    def perimeter(self):
        """Возвращает периметр пирамиды"""
        return 2 * super().perimeter + 2 * self.side


pyramid = Pyramid(6, 4)
print(pyramid.square)
print(pyramid.perimeter)

cube = Cube(5)
print(cube.square)
print(cube.perimeter)
