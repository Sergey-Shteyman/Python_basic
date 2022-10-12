# quantity_records = int(input("Сколько записей вносится в протокол? "))
# print("Записи (результат и имя):")
# players_results = dict()
# for index in range(quantity_records):
#     user_input = tuple(input(f"{index + 1}-я запись: ").split(" "))
#     players_results[index] = user_input

# players_results = {
#     0: (69485, 'Jack'),
#     1: (95715, 'qwerty'),
#     2: (95715, 'Alex'),
#     3: (83647, 'M'),
#     4: (197128, 'qwerty'),
#     5: (95715, 'Jack'),
#     6: (93289, 'Alex'),
#     7: (95715, 'Alex'),
#     8: (95715, 'M')
# }
#
# print("Итоги соревнований: ")
# winers = dict()
# for index in range(3):
#     winner = max(players_results.values())
#     print(f"{index + 1}-е место. {winner[1]} ({winner[0]})")
#     players_results = {key: val for key, val in players_results.items() if val != winner}


def score_key(a):
    return a[1][0] * 100000000 - a[1][1]


score_table = {}
number_rows = int(input('Общее количество строк протокола: '))
print('Введите результат - имя участника (через пробел)')
for time in range(number_rows):
    ball, name = input('{0} запись:'.format(time + 1)).split()
    ball = int(ball)
    if name in score_table:
        if ball > score_table[name][0]:
            score_table[name][0] = ball
            score_table[name][1] = time
    else:
        score_table[name] = [ball, time]
scores = list(score_table.items())

scores.sort(key=score_key, reverse=True)
print('\nИтоги соревнований: ')
for winner_index in 0, 1, 2:
    print(f'{winner_index + 1} место {scores[winner_index][0]}', end=' ')
    print(f'({scores[winner_index][1][0]})', sep='')
