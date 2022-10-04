groups_of_numbers = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
numbers = [num for heap in groups_of_numbers
            for element in heap
            for num in element]
print(numbers)