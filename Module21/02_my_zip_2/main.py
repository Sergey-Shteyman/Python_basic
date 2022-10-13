# First Solution

def my_zip(*args):
    length = min(len(element) for element in args)
    result_collection = [
        tuple(struct[index] for struct in map(list, args)) for index in range(length)
    ]
    return result_collection


first_collection = [1, 2, 3, 4, 5]
second_collection = {1: "s", 2: "q", 3: 4}
third_collection = (1, 2, 3, 4, 5)
print(my_zip(first_collection, second_collection, third_collection))

# Second solution

# def my_zip(chars, numbers, length):
#     if length < 1:
#         return 0
#     result = my_zip(chars, numbers, length - 1)
#     print((chars[result], numbers[result]))
#     return length
#
#
# chars = list(input("Строка: "))
# numbers = input("Кортеж чисел (через пробел): ").split(" ")
# total_length = min(len(chars), len(numbers))
# result = my_zip(chars, numbers, total_length)


