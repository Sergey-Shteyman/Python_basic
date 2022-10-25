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

book = open(os.path.abspath("voyna-i-mir.txt"), 'r', encoding='utf-8')
text_book = book.read()
char_quantity = {}
letters = 0
for letter in text_book:
    if letter.isalpha():
        quantity = char_quantity.get(letter, 0)
        char_quantity[letter] = quantity + 1
        letters += 1
count_letter_dict = [
    (index, "{:8.6f}".format(char_quantity[index] / letters)) for index in char_quantity.keys()
]
book.close()
count_letter_dict.sort(key=lambda argument: argument[1], reverse=True)
print()
for i_elem in count_letter_dict:
    print(i_elem[0] + " " + i_elem[1])
