import os


def summ_numbers(file_name):
    data = open(file_name, "r")
    summ = 0
    for i_elem in str(data):
        if i_elem.isdigit():
            summ += int(i_elem)
    data.close()
    write_summ(summ)


def write_summ(numbers):
    answer = open("answer.txt", "w")
    answer.write(str(numbers))
    answer.close()


numbers_file = "numbers.txt"
summ_numbers(numbers_file)
