from math import pi
from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный базовый класс"""

    def __init__(self, x_pos, y_pos, length=None, width=None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos


class MyMathMixin:
    @classmethod
    def circle_len(cls, radius):
        return 2 * pi * radius

    @classmethod
    def circle_square(cls, radius):
        return pi * radius ** 2

    @classmethod
    def volume_cube(cls, side):
        return side ** 3

    @classmethod
    def area_surface_square_sphere(cls, radius):
        return 4 * pi * radius ** 2


class Circle(Figure, MyMathMixin):
    """Класс окружность"""

    def move(self, x_pos, y_pos):
        super().move(x_pos, y_pos)

    def coordinates(self):
        return self.x_pos, self.y_pos


circle_1 = Circle(x_pos=10, y_pos=10)
circle_2 = Circle(x_pos=0, y_pos=0)
square_circle = circle_1.circle_square(4)
lenght_circle = circle_2.circle_len(4)
print(f"Площадь окружности c координатами в точках "
      f"{circle_1.coordinates()} равна {square_circle}")
print(f"Длина окружности c координатами в точках "
      f"{circle_2.coordinates()} равна {lenght_circle}")
