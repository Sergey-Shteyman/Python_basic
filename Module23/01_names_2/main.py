summ = 0
line_count = 0
name_file = "people.txt"
error_not_found_file = f"ОШИБКА: файл {name_file} не обнаружен"
error_length_name = 'ОШИБКА: длина {} строки меньше трех символов в строке'

try:
    with open(name_file, "r", encoding='utf-8') as peopl:
        names = peopl.read().split('\n')
        for person in names:
            line_count += 1
            summ += len(person)
            try:
                if len(person) < 3:
                    raise BaseException
            except BaseException:
                print(error_length_name.format(line_count))
                with open('errors.log', 'w') as errors:
                    errors.write(error_length_name.format(line_count))
        print(f"Общее количество символов: {summ}")

except FileNotFoundError:
    print(error_not_found_file)
    with open('errors.log', 'w') as errors:
        errors.write(f"ОШИБКА: файл {name_file} не обнаружен")
