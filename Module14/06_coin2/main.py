def coin_coordinates(x, y, r):
    if x * x + y * y <= r * r:
        return "Монетка где-то рядом"
    else:
        return "Монетки в области нет"


print("Введите координаты монетки: ")
x = float(input("X: "))
y = float(input("Y: "))
r = float(input("Введите радиус: "))
print("-" * 20)
print(coin_coordinates(x, y, r))

