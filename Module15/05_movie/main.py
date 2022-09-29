films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
likes = []
def movie_selection():
    name_film = input("Введите название фильма: ")
    if likes.__contains__(name_film):
        print("Вы уже выбрали данный фильм, пожалуйста, выберете другой фильм")
        movie_selection()
    elif films.__contains__(name_film):
        likes.append(name_film)
    else:
        print("Такого фильма в списке нет!")
    answer = input("Хотите продолжить выбор фильма? y/n: ")
    if answer == "y" or answer == "Y":
        movie_selection()
    else:
        print(f"Весь список фильмов {films}", sep='\n')
        print(f"Список любимых фильмов {likes}")

movie_selection()