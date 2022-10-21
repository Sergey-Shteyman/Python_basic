from typing import Iterable


def finde_sum(*args):
    return sum(finde_sum(*arg) if isinstance(arg, Iterable) else arg for arg in args)


result = finde_sum([[1, 2, [3]], [1], 3])
print(f"Ответ в консоли: {result}")
