def danger_jears(jear_1, jear_2):
    for i in range(jear_1, jear_2 + 1):
        for j in range(0, 10):
            if str(i).count(str(j)) == 3:
                print(i)


jear_1 = int(input("Введите первый год: "))
jear_2 = int(input("Введите второй год: "))
print('-' * 20)
print(f"Года от {jear_1} до {jear_2} с тремя одинаковыми цифрами:")
danger_jears(jear_1, jear_2)
