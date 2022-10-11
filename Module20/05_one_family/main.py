all_families_dict = {
    1: {
        "Сидоров Никита": 35,
        "Сидорова Алина": 34,
        "Сидоров Павел": 10
    },
    2: {
        "Абобов Акакий": 115,
        "Абобова Зульфия": 112,
        "Абобов Корнеплод": 9,
        "Абобова Кочебрыжка": 10
    }
}

family = input("Введите фамилию: ").lower()

if list(family)[-1] == 'a':
    family = family[::-1]
    print(family)

for key in all_families_dict.keys():
    for values in all_families_dict[key].keys():
        if family[:-1] in values.lower():
            print(values, " ", all_families_dict[key][values])
