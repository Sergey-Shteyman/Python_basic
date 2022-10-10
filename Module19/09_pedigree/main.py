number_people = int(input('Введите количество человек: '))
data = dict()
levels = dict()

for i in range(1, number_people):
    descendant_name, parent_name = input(f'{i} пара: ').split()
    data[descendant_name] = parent_name
    levels[descendant_name] = 0
    levels[parent_name] = 0

for i in data:
    people = i
    while people in data:
        people = data[people]
        levels[i] += 1

print('\n“Высота” каждого члена семьи:')
for i in sorted(levels):
    print(i, levels[i])
