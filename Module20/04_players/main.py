players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


def unification_data(players):
    return [key + value for key, value in players.items()]


print(unification_data(players))