n = int(input("Ввудите целое число N: "))
list = []
for i in range(1, n + 1):
    if i % 2 != 0:
        list.append(i)
print(list)
