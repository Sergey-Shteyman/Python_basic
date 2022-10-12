def crypto(collection):
    return [number for index, number in enumerate(collection[2:], start=2) if is_prime(index)]


def is_prime(number):
    counter = 0
    for digit in range(2, number // 2 + 1):
        if number % digit == 0:
            counter = counter + 1
    if counter <= 0:
        return True
    else:
        return False


prime_indexes = crypto('О Дивный Новый мир!')
print(prime_indexes)
