user_input = input("Ввеите IP: ")
def correct_ip_(user_input):
    user_input = user_input.split(".")
    if len(user_input) != 4:
        print("Адрес — это четыре числа, разделённые точками.")
        return
    else:
        for item in user_input:
            if not item.isdigit():
                print(f"{item} - это не целое число")
                return
            elif int(item) > 255:
                print(f"{item} - превышает 255")
                return
    print("IP-адрес корректен.")
    return


correct_ip_(user_input)
