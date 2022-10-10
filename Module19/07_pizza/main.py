def get_key(dictionary, value):
    for keys, values in dictionary.items():
        if values == value:
            return keys


countity_orders = int(input("Введите колличество заказов: "))
client_orders = dict()

for index in range(1, countity_orders + 1):
    user_input = input(f"{index}-й заказ: ").split(" ")
    if user_input[0] not in client_orders:
        client_orders[user_input[0]] = {user_input[1]: int(user_input[2])}
    else:
        if user_input[1] not in client_orders[user_input[0]]:
            client_orders[user_input[0]][user_input[1]] = int(user_input[2])
        else:
            client_orders[user_input[0]][user_input[1]] += int(user_input[2])


for client, order in client_orders.items():
    print(f"{client}:")
    for pizza, quantity in order.items():
        print(f"{' ' * 7}{pizza}: {quantity}")


