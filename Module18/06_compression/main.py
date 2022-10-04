def compress(str_txt):
    str_len = len(str_txt)
    result = ''

    if str_len > 0:
        index = 0
        while index < str_len:
            counter = 0
            curr_char = str_txt[index:index + 1]
            while index < str_len and str_txt[index] == curr_char:
                index += 1
                counter += 1
            result += curr_char + str(counter)
    return result


text = input('Введите строку: ')
print(compress(text))

