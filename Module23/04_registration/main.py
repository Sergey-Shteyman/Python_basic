
def registration():
    registrations_bad = "registrations_bad.log"
    registration_good = "registrations_good.log"
    user_input = input("Введите ваше имя, имейл, "
                       "возраст через пробел: ").split(" ")
    try:
        if len(user_input) == 3:
            if user_input[0].isalpha():
                if '@' in user_input[1] and '.' in user_input[1]:
                    if int(user_input[2]) >= 10 and int(user_input[2]) < 100:
                        with open(registration_good, "a", encoding="utf-8") as user_data:
                            user_data.write(f"{' '.join(user_input)}\n")
                    else:
                        raise ValueError
                else:
                    raise SyntaxError
            else:
                raise NameError
        else:
            raise IndexError

    except IndexError:
        with open(registrations_bad, "a", encoding='utf-8') as user_errors:
            error_line = f"{' '.join(user_input)} {' ' * 5}" \
                         f"НЕ присутствуют все три поля\n"
            user_errors.write(error_line)
    except NameError:
        with open(registrations_bad, "a", encoding='utf-8') as user_errors:
            error_line = f"{' '.join(user_input)} {' ' * 5}" \
                         f"Поле «Имя» содержит НЕ только буквы\n"
            user_errors.write(error_line)
    except SyntaxError:
        with open(registrations_bad, "a", encoding='utf-8') as user_errors:
            error_line = f"{' '.join(user_input)} {' ' * 5}" \
                         f"Поле «Имейл» НЕ содержит @ и . (точку)\n"
            user_errors.write(error_line)
    except ValueError:
        with open(registrations_bad, "a", encoding='utf-8') as user_errors:
            error_line = f"{' '.join(user_input)} {' ' * 5}" \
                         f"Поле «Возраст» НЕ является числом от 10 до 99\n"
            user_errors.write(error_line)



registration()