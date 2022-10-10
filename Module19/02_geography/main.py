quantity_countries = int(input("Количество стран: "))
cities_in_country = dict()
for index in range(0, quantity_countries):
    countries = (input(f"{index + 1}-я страна: ")).split()
    for city in countries[1:]:
        cities_in_country[city] = countries[0]

for step in range(1, 4):
    user_input = input(f"\n{step}-й город: ")
    country = cities_in_country.get(user_input)
    if country:
        print(f"Город {user_input} расположен в стране {country}.")
    else:
        print(f"По городу {user_input} данных нет.")
