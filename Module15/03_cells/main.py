listCount = int(input("Кол-во клеток: "))
effectiveness = []
inefficient = []
for i in range(1, listCount + 1):
    print(f"Эффеективность {i} клетки: ", end='')
    value = int(input())
    effectiveness.append(value)
    if value < i:
        inefficient.append(value)
if len(inefficient) != 0:
    print("Неподходящие значения: ", end='')
    for i in inefficient:
        print(i, end=' ')
else:
    print("Все клетки подходят!")