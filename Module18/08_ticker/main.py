first_input = input("Первая строка: ")
second_input = input("Вторая строка: ")

if first_input == second_input:
    print("\nСтроки идентичны.")
elif len(second_input) != len(first_input):
    print("\nОдна из строк больше другой.")
else:
    counter = 1
    flag = False
    for index in range(len(second_input) - 1):
        second_input = second_input[-1] + second_input[:-1]
        if second_input == first_input:
            flag = True
            print(f"\nПервая строка получается из второй со здвигом {counter}.")
            break
        else:
            counter += 1
    if not flag:
        print("\nПервую строку нельзя получить из второй с помощью циклического сдвига.")