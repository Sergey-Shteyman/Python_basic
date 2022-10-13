def recursive_output(number):
    if number < 1:
        return 1
    recursive_output(number - 1)
    print(number)
    return number


user_input = int(input("Введите число: "))
recursive_output(user_input)
