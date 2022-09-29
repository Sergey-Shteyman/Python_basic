# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# TODO переписать программу

first_main_lst = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_lst = [1, 3, 1, 5, 3, 3]
first_main_lst += second_list
count_numbers = first_main_lst.count(5)
print("Результат работы программы:", end='\n')
print("Кол-во цифр 5 при первом объединении: ", count_numbers, end='\n')
for num in first_main_lst:
    if num == 5:
        first_main_lst.remove(num)
first_main_lst += third_lst
count_numbers = first_main_lst.count(3)
print("Кол-во цифр 3 при втором объединении: ", count_numbers, end='\n')
print("Итоговый список: ", first_main_lst)
