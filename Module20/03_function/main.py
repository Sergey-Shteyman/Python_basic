def slicer(numbers_collection, random_number=0):
    if random_number == 0:
        return tuple()
    elif numbers_collection.count(random_number) > 1:
        first_index = numbers_collection.index(random_number)
        last_index = numbers_collection.index(random_number, first_index + 1) + 1
        new_slice = numbers_collection[first_index:last_index]
        return new_slice
    else:
        return numbers_collection[numbers_collection.index(random_number):]


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
