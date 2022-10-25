import random


def summation(x_coordinate, y_coordinate):
    x_coordinate += random.randint(0, 10)
    y_coordinate += random.randint(0, 5)
    return x_coordinate / y_coordinate


def subtraction(x_coordinate, y_coordinate):
    x_coordinate -= random.randint(0, 10)
    y_coordinate -= random.randint(0, 5)
    return y_coordinate / x_coordinate


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            res1 = summation(int(nums_list[0]), int(nums_list[1]))
            res2 = subtraction(int(nums_list[0]), int(nums_list[1]))
            try:
                number = random.randint(0, 100)
                with open('result.txt', 'w') as file_2:
                    my_list = sorted([res1, res2, number])
                    file_2.write(' '.join(my_list))
            except FileNotFoundError:
                print("Что-то пошло не так : ")
except FileNotFoundError:
    print("File 'coordinatex.txt' not found")