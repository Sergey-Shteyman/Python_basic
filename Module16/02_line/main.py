# TODO здесь писать код
def sorted_lst(lst):
    for step in range(len(lst) - 1):
        for index in range(len(lst) - 1 - step):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst


first_class = list(range(160, 176, 2))
second_class = list(range(162, 180, 3))
first_class.extend(second_class)
sorted_class = sorted_lst(first_class)
print(f"Отсортированный список учеников: {sorted_class}")
