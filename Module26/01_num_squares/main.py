class SquaresOfNumbers:
    """Генерация квадратов чисел с помощью итератора"""

    def __init__(self, limit: int):
        self.limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.limit:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration


squares_of_numbers_with_iterator = SquaresOfNumbers(10)
print("С помощью класса итератора:")
for num in squares_of_numbers_with_iterator:
    print(num, end=' ')


def generation_squares_of_numbers(limit: int, counter=0):
    """Генерация квадратов чисел с помощью генератора"""
    while counter < limit:
        counter += 1
        yield counter ** 2
    else:
        return


print("\nС помощью генератора:")
for num in generation_squares_of_numbers(10):
    print(num, end=' ')


squares_numbers = (num**2 for num in range(11))
print('\nС помощью генераторного выражения')
for num in squares_numbers:
    print(num, end=' ')

