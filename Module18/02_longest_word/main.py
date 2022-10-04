user_input = input("Введите строку: ").split(" ")
longest_word = max(user_input, key=len)
len_of_longest_word = len(longest_word)
print(f"Самое длинное слово: {longest_word}"
      f"\nДлина этого слова: {len_of_longest_word}")
