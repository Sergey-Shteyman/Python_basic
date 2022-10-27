class Circle:
    pi = 3.14159

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        return self.r * self.r * self.pi

    def get_perimeter(self):
        return 2 * self.r * self.pi

    def scale(self, k):
        self.r *= k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2


first_circle = Circle(1, 1, 1)
second_circle = Circle(0, 0, 2)

print(f"Площадь круга 1 равна: {first_circle.get_area()}")
print(f"Периметр круга 1 равна: {first_circle.get_perimeter()}")
first_circle.scale(2)
print("Круг 1 увеличился в 2 раза")
print(f"Площадь круга 1 равна: {first_circle.get_area()}")
print(f"Пересекается ли круг 1 с кругом 2: {first_circle.is_intersect(second_circle)}")
