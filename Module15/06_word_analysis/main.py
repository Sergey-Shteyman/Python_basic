word = input("Введите слово: ")
count_list = []
count_same = 0
for i in word:
    if word.count(i) == 1:
        count_same += 1
print("Кол-во уникальных букв: ", count_same)
