import re

telephone_numbers = [
    '9999999999', '999999-999',
    '99999x9999', '89109664445',
    '89109664445554', "8910664",
    '9123456789'
]

valid_number_pattern = r"[8, 9]\d{9}\b"

for number in telephone_numbers:
    if re.match(valid_number_pattern, number):
        print(f"Номер: {number} подходит")
    else:
        print(f"Номер: {number} НЕ подходит")
