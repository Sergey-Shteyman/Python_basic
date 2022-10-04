def get_index(smb, to_right, encoding_lst):
    index = encoding_lst.index(smb)
    if index + to_right > len(encoding_lst) - 1:
        index = index + to_right - len(encoding_lst)
    else:
        index += to_right
    return index


text = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

ascii_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ascii_ru = [chr(i) for i in range(ord('а'), ord('я') + 1)]
encrypted_string = ''

for symbol in text:
    if symbol in ascii_ru:
        encrypted_string += ascii_ru[get_index(symbol, shift, ascii_ru)]
    elif symbol in ascii_en:
        encrypted_string += ascii_en[get_index(symbol, shift, ascii_en)]
    else:
        encrypted_string += symbol

print(encrypted_string)

# MARK: - Еще один способ решения

# def offset_by_uni(shift, lst):
#     lst_with_shift = []
#     for char in lst:
#         if ord(char) + shift > ord("я"):
#             lst_with_shift.append(chr(ord(char) + shift - 32))
#         elif ord(char) + shift < ord("а"):
#             lst_with_shift.append(chr(ord(char) + shift + 32))
#         else:
#             lst_with_shift.append(chr(ord(char) + shift))
#     return lst_with_shift
#
# def caesar_cipher():
#     user_str = input("Введите сообщение: ")
#     shift = int(input("Введите сдвиг: "))
#     user_lst = offset_by_uni(shift, list(user_str))
#
#     if user_str.count(" ") > 0:
#         spaces_positions = [position for position in range(len(user_str))
#                             if user_str[position] == " "]
#         for position in spaces_positions:
#             user_lst.pop(position)
#             user_lst.insert(position, " ")
#         user_str = "".join(user_lst)
#         print(f"Зашифрованное сообщение: {user_str}")
#     else:
#         user_str = "".join(user_lst)
#         print(f"Зашифрованное сообщение: {user_str}")
#
#
# caesar_cipher()


