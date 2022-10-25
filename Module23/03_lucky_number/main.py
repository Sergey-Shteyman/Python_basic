import random


def lucky_number(name_file):
    try:
        with open(name_file, 'a') as out_file:
            lucky_sum = 0
            while lucky_sum < 777:
                random_number = random.randint(1, 13)
                if random_number != 13:
                    user_input = int(input("Введите число: "))
                    lucky_sum += user_input
                    out_file.write(f"{str(user_input)}\n")
                else:
                    raise BaseException
            print("Вы успешно выполнили условие для выхода из порочного цикла!")
    except FileNotFoundError:
        print(f"CustomError: {name_file} not found")
    except BaseException:
        print("Вас постигла неудача!")
    return


numbers_input = list()
name_file = "out_file.txt"
lucky_number(name_file)


# Second solution, but doesn't work correct

# def lucky_number(name_file, lucky_sum=0):
#     try:
#         with open(name_file, 'a') as out_file:
#             user_input = int(input("Введите число: "))
#             lucky_sum += user_input
#             numbers_input.append(user_input)
#             if lucky_sum >= 777:
#                 out_file.write(f"{str(user_input)}\n")
#                 print("Вы успешно выполнили условие "
#                       "для выхода из порочного цикла!")
#                 for numbers in numbers_input[::-1]:
#                     out_file.write(f"{str(numbers)}\n")
#                 return
#             else:
#                 # out_file.write(f"{str(user_input)}\n")
#                 return lucky_number(name_file, lucky_sum)
#     except FileNotFoundError:
#         print(f"CustomError: {name_file} not found")
#     return