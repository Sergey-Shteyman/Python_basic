word = input("Введите слово: ")
count_list = []
count_same = 0
for char in word:
    if word.count(char) == 1:
        count_same += 1
print("Кол-во уникальных букв: ", count_same)
