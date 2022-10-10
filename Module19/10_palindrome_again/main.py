word = input("Введите строку: ").lower()
chars = set()

for char in word:
    if char not in chars:
        chars.add(char)
    else:
        chars.remove(char)
if len(chars) > 1:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")
