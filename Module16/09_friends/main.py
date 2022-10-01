friend = int(input('Кол-во друзей: '))
receipt = int(input('Долговых расписок: '))
friends_lst = []

for _ in range(friend):
    friends_lst.append(0)

for number in range(receipt):
    print(f'\n{number + 1} расписка')
    to_who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_lst[from_who - 1] += how_much
    friends_lst[to_who - 1] -= how_much

print('\nБаланс друзей:')
for index in range(len(friends_lst)):
    print(f'{index + 1} : {friends_lst[index]}')
