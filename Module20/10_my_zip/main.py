def my_zip(chars, numbers):
    return ((chars[index], numbers[index]) for index in range(len(min(chars, numbers))))


chars = list(input("Строка: "))
print(chars)
numbers = input("Кортеж чисел (через пробел): ").split(" ")
result = my_zip(chars, numbers)
print("\nРезультат:", result, sep='\n')
for item in result:
    print(item)

