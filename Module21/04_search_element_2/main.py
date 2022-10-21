site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth=None):
    if depth:
        if depth == 1:
            if key in struct:
                return struct[key]
        if depth > 1:
            for sub_struct in struct.values():
                if isinstance(sub_struct, dict):
                    result = find_key(sub_struct, key, depth - 1)
                    if result:
                        break
            else:
                result = None
            return result
    else:
        if key in struct:
            return struct[key]
        for value in struct.values():
            if isinstance(value, dict):
                result = find_key(value, key)
                if result:
                    break
        else:
            result = None

        return result


def user_answer():
    user_input = input("Введите искомый ключ: ")
    user_deep = input("Хотите ввести максимальную глубину? Y/N: ")
    if user_deep == 'n':
        value_key = find_key(site, user_input)
        print(f"Значение ключа: {value_key}")
    elif user_deep == 'y':
        maximum_deep = int(input("Введите максимальную глубину: "))
        value_key = find_key(site, user_input, maximum_deep)
        print(f"Значение ключа: {value_key}")
    else:
        print("Некорректный ответ. Попробуйте еще раз...")
        user_answer()


user_answer()



