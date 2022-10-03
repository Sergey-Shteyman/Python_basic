import random

quantity_sticks = int(input("Количество палок: "))
quantity_throws = int(input("Количество бросков: "))
result = ["I" for _ in range(quantity_sticks)]
for throw in range(1, quantity_throws + 1):
    first_shot = random.randint(1, 10)
    second_shot = random.randint(first_shot, 10)
    shots = [first_shot, second_shot]
    for index in range(first_shot - 1, second_shot):
        result.pop(index)
        result.insert(index, ".")
    print(f"Бросок {throw}. Сбиты палки с номера {shots[0]} по номер {shots[1]}")
result_str = "".join(result)
print(f"\nРезультат: {result_str}")


