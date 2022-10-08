maximum_number = int(input("Введите максимальное число: "))
all_numbers = set(range(1, maximum_number + 1))

while True:
    user_input = input("Нужное число есть среди вот этих чисел: ").lower()
    if user_input == 'помогите!':
        break
    user_input = {int(num) for num in user_input.split()}
    answer = input("Ответ Артема: ").lower()
    if answer == 'да':
        all_numbers &= user_input
    else:
        all_numbers -= user_input

print("Артём мог загадать следующие числа:", *all_numbers)
