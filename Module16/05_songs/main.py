violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def music_selection(playlist):
    quantity_songs = int(input("Сколько песен выбрать? "))
    favorite_tracks = []
    amount_time_hearing = 0
    for index in range(1, quantity_songs + 1, 1):
        print(f"Название {index}-й песни: ", end='')
        favorite_tracks.append(input())
    for song in playlist:
        if favorite_tracks.__contains__(song[0]):
            amount_time_hearing += song[1]
    print(f"\nОбщее время звучания песен: {round(amount_time_hearing, 2)}")


music_selection(violator_songs)