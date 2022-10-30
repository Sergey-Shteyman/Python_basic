class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


def taxes():
    user_money = int(input("Введите количество денег, которые у вас есть: "))
    user_car = int(input("Введите стоимость машины: "))
    tax_car = Car(user_car).tax()
    print(f"Стоимость налога на машину: {tax_car}")
    user_apart = int(input("Введите стоимость апартаментов: "))
    tax_apart = Apartment(user_apart).tax()
    print(f"Стоимость налога на апартамента: {tax_apart}")
    user_country_house = int(input("Введите стоимость загородного дома: "))
    tax_country_house = CountryHouse(user_country_house).tax()
    print(f"Стоимость налога на загородный дом: {tax_country_house}")

    tax_amount = tax_car + tax_apart + tax_country_house
    print(f"Всего налогов нужно заплатить: {tax_amount}")

    if tax_amount < user_money:
        remaining_money = user_money - tax_amount
        print(f"Вы успешно заплатили все налоги\n"
              f"У вас осталось денег: {remaining_money}")
    else:
        remaining_taxes = tax_amount - user_money
        print(f"У вас не хватает денег, чтобы заплатить налоги!\n"
              f"Столько денег нужно заплатить: {remaining_taxes}")

    print("\n Конец работы программы..")

taxes()
