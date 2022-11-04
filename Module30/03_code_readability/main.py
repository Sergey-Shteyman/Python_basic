simple_numbers_part_1 = list(filter(lambda num_i: num_i > 1 and not all(
    num_i % num_j == 0 for num_j in range(1, num_i)), range(1000)))


def simple_numbers_part_2():
    """Simple Numbers"""
    simple_numbers = list()
    for i_num in range(1, 1000):
        if not all(i_num % j_num == 0 for j_num in range(1, i_num)):
            simple_numbers.append(i_num)
    return simple_numbers


if __name__ == "__main__":
    print(simple_numbers_part_1)
    print(simple_numbers_part_2())
