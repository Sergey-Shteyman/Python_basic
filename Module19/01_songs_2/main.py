violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
enumerations = [
    "первой", "второй", "третей", "четвертой",
    "пятой", "шестой", "седьмой", "восьмой", "девятой"
]
total_time = 0
user_input = int(input("Сколько песен выбрать? "))
user_songs = [input(f"Название {enumerations[index]} песни: ") for index in range(user_input)]
for index in range(len(user_songs)):
    if user_songs[index] in violator_songs:
        total_time += violator_songs[user_songs[index]]
print(f"Общее время звучания песен: {round(total_time, 2)}")


