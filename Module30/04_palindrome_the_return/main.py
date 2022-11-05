from collections import Counter


# Не совсем понял задание. Можно в каком плане? Путем добавления скольких символов?
# Если одного, то вот решение:
def can_be_poly(chars: str) -> bool:
    return len(list(filter(lambda value: value % 2, Counter(chars).values()))) <= 2

# print(can_be_poly("baa"))

# Проверка на полиндром на всякий:

def can_be_poly_part_2(chars: any) -> bool:
    if str(chars) == str(chars)[::-1]:
        return True
    return False


print(can_be_poly_part_2("baa"))
print(can_be_poly_part_2("baab"))