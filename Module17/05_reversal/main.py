str = input("Введите строку в которой буква h встречается как минимум два раза: ")
sequence = str[str.rindex("h") - 1:str.index("h"):-1]
print(sequence)
