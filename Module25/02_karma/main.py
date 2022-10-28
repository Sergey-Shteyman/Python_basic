import karma


def life():
    print("----Добро пожаловать в игру под названием жизнь!----")
    current_life_points = 0
    errors_file_name = "karma.log"
    while current_life_points < karma.Karma().get_karma():
        response = karma.Karma().one_day()
        if isinstance(response, int):
            current_life_points += response
        else:
            print(response.__str__())
            with open(errors_file_name, "a") as errors:
                errors.write(response.__str__())
                break
        print(f"Набрано очков жизни: {current_life_points}")
    if current_life_points >= 500:
        print("Поздравляем, вы успешно прожили жизнь и достигли нирваны!)")


life()
