shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_of_details = input("Введите название детали: ")
count_details = 0
total_amount = 0
for product in shop:
        if product[0] == name_of_details:
                count_details += 1
                total_amount += product[1]
print(f"Кол-во деталей — {count_details}")
print(f"Общая стоимость — {total_amount}")
