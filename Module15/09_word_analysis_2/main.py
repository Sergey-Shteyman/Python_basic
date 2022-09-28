lst_word = list(input("Введите ваше слово: "))
if lst_word == lst_word[::-1]:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")