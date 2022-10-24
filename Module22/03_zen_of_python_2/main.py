zen_python = open("zen.txt", "r")

data = zen_python.read().lower().split("\n")
count_chars = 0
count_enters = len(data)
count_words = len(str(data).split(" "))
chars = dict()

for char in str(data):
    if char.isalpha():
        count_chars += 1
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

rare_char = min(chars, key=chars.get)
quantity_rare_char = chars[rare_char]

zen_python.close()
print(f"Количество букв в файле: {count_chars}")
print(f"Количество слов в файле: {count_words}")
print(f"Колличество строк в файле: {count_enters}")
print(f"Наиболее редкая буква: {rare_char} - {quantity_rare_char}")
