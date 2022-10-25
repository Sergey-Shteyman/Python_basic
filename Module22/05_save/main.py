import os


def save_text(text, way, filename):
    # Users sergejstejman PycharmProjects Python_Basic Module22 05_save
    abs_path = os.path.abspath(filename)
    check_file = os.path.exists(abs_path)
    if check_file:
        ans_q = input(f'Вы действительно хотите перезаписать файл? \n')
        if ans_q == 'да':
            with open(filename, 'w') as file_object:
                file_object.write(text)
                print(f'Файл успешно перезаписан!')
        else:
            print(f'Data is not record')
    else:
        with open(filename, 'w') as file_object:
            file_object.write(text)
            print(f'Файл успешно сохранён!')


text = str(input(f'Введите строку: '))
path = str(input(
    f'Куда хотите сохранить документ? '
    f'Введите последовательность папок (через пробел): '))
filename = str(input(f'Введите имя файла: '))

save_text(text, path, filename)
