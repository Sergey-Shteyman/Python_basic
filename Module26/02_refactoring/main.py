list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def necessary_result(to_find):
    for i_num in list_1:
        for j_num in list_2:
            result = i_num * j_num
            yield i_num, j_num, result
            if result == to_find:
                print('Found!!!')
                return


for num in necessary_result(to_find):
    print(*num)
