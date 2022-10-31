import karma


def try_to_live_life_and_achieve_nirvana():
    print("----Добро пожаловать в игру под названием жизнь!----")
    current_life_points = 0
    while current_life_points < karma.Karma().get_karma():
        response = karma.Karma().one_day()
        if isinstance(response, int):
            current_life_points += response
        print(f"Набрано очков жизни: {current_life_points}")
    if current_life_points >= 500:
        print("Поздравляем, вы успешно прожили жизнь и достигли нирваны!)")


try_to_live_life_and_achieve_nirvana()
