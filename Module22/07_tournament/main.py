new_file = open("first_tour.txt", "r", encoding="utf8")
line_file = int(new_file.readline())

new_list = []

for line in new_file:
    new_line = line.split()

    if new_line != [] and int(new_line[-1]) > line_file:
        new_list.append(new_line)
new_file.close()

new_list.sort(key=lambda element: int(element[-1]))
new_list.reverse()

count = str(len(new_list))

out_lst = []
count_players = 1
for index in new_list:
    name_sim = str(index[0][0]) + '.'
    s_win = str(count_players) + ') ' + name_sim + ' ' + index[1] + ' ' + index[-1]
    out_lst.append(s_win)
    count_players += 1

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(count + '\n')
    command = '\n'.join(out_lst)
    f_out.write(command)

for index in out_lst:
    print(f'{index}')
