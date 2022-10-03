text = input("Введите текст: ")
vowels_letters = "аоиеёэыуюя"
vowel_chars_text = [char for char in text if char in vowels_letters]
length = len(vowel_chars_text)
print(f"\nСписок гласных букв: {vowel_chars_text}", end="\n")
print(f"Длина списка: {length}")

