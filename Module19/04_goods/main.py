goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def get_key(dictionary, value):
    for keys, values in dictionary.items():
        if values == value:
            return keys


for product, value in store.items():
    quantity = 0
    price_per_item = 0
    total_product_price = 0
    for item in value:
        quantity += item["quantity"]
        price_per_item += item["price"]
        total_product_price += item["quantity"] * item["price"]
    print(f"{get_key(goods, product)} - {quantity} штук,"
          f" стоимость {total_product_price:} рубля")
