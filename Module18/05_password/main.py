while True:
    user_password = input("Придумайте пароль: ")
    quantity_numbers = 0
    quantity_upper_chars = 0

    for symbol in user_password:
        if symbol.isdigit():
            quantity_numbers += 1
        if symbol.isupper():
            quantity_upper_chars += 1

    if quantity_upper_chars >= 2 and quantity_numbers >= 3:
        print("Это надёжный пароль!")
        break
    else:
        print("Попробуйте ещё раз.")
