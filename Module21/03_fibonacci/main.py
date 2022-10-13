def fibonacci(number):
    if number in (1, 2):
        return 1
    result = fibonacci(number - 1) + fibonacci(number - 2)
    return result


user_input = int(input("Введите позицию числа в ряде Фибоначчи: "))
number_fibonacci = fibonacci(user_input)
print(f"Число {number_fibonacci}")
