def unique_elements():
    first_lst = []
    second_lst = []
    for index in range(1, 4):
        print(f"Введите {index}-е число для первого списка: ", end='')
        first_lst.append(int(input()))
    print("")
    for index in range(1, 8):
        print(f"Введите {index}-е число для первого списка: ", end='')
        second_lst.append(int(input()))
    print(f"Первый список: {first_lst}")
    print(f"Второй список: {second_lst}")
    first_lst.extend(second_lst)
    for num in first_lst:
        if first_lst.count(num) > 1:
            first_lst.remove(num)
    print(f"\nНовый первый список с уникальными элементами: {first_lst}")


unique_elements()