import os
import zipfile

#Не понимаю почему не сработало..(
# archive = os.path.abspath("voyna-i-mir.zip")
# directory_to_extract_to = os.path.abspath("09_war_and_peace")
# # with zipfile.ZipFile(archive, 'r') as zip_file:
# #     zip_file.extractall(directory_to_extract_to)
# extracted_arhive = zipfile.ZipFile(archive)
# extracted_arhive.extractall(directory_to_extract_to)
# extracted_arhive.close()

str_open = open(os.path.abspath("voyna-i-mir.txt"), 'r', encoding='utf-8')
list_file = str_open.read()
count_dict = {}
count_letter = 0
for letter in list_file:
    if letter.isalpha():
        x = count_dict.get(letter, 0)
        count_dict[letter] = x + 1
        count_letter += 1
count_letter_dict = [(k, "{:8.6f}".format(count_dict[k] / count_letter)) for k in count_dict.keys()]
str_open.close()
count_letter_dict.sort(key=lambda x: x[1], reverse=True)
print()
for i in count_letter_dict:
    print(i[0] + " " + i[1])
