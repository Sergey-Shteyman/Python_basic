name_file = input("Название файла: ")
special_symbols = "@№$%^&\*()"
extensions = [".txt", ".docx"]
if name_file[0] in special_symbols:
    print(f"\nОшибка: название начинается на один из специальных символов. "
          f"Remove this: {name_file[0]}")
elif not name_file.endswith(extensions[0]) and not name_file.endswith(extensions[1]):
    print("\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("\nФайл назван верно.")
