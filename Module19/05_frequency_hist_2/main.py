user_input = input("Введите текст: ")
print("Оригинальный словарь частот:")
original_frequencies = dict()
inverted_frequencies = dict()
for char in user_input:
    original_frequencies[char] = user_input.count(char)
for key in sorted(original_frequencies.keys()):
    print(f"{key} : {original_frequencies[key]}")
print("\nИнвертированный словарь частот:")
for char, number in original_frequencies.items():
    inverted_frequencies.setdefault(number, []).append(char)
for char in inverted_frequencies:
    print(char, ': ', inverted_frequencies[i], sep='')
