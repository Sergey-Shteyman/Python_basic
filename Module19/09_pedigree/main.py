number_people = int(input('Введите количество человек: '))
data = dict()
levels = dict()

for number in range(1, number_people):
    descendant_name, parent_name = input(f'{number} пара: ').split()
    data[descendant_name] = parent_name
    levels[descendant_name] = 0
    levels[parent_name] = 0

for index in data:
    people = index
    while people in data:
        people = data[people]
        levels[index] += 1

print('\n“Высота” каждого члена семьи:')
for index in sorted(levels):
    print(index, levels[index])
