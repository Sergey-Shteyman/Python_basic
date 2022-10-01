people = int(input('Кол-во человек: '))
dropped = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', dropped, 'человек.')
people_lst = list(range(1, people + 1))
out = 0

for _ in range(people - 1):
    print('\nТекущий круг людей', people_lst)
    start_count = out % len(people_lst)
    out = (start_count + dropped - 1) % len(people_lst)
    print('Начало счёта с номера', people_lst[start_count])
    print('Выбывает человек под номером', people_lst[out])
    people_lst.remove(people_lst[out])

print('\nОстался человек под номером', *people_lst)
