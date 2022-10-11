numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first_solution = [
    (numbers[index], numbers[index + 1]) for index in range(0, len(numbers) - 1, 2)
]
second_solution = list(zip(numbers[::2], numbers[1::2]))
print(first_solution)
print(second_solution)
