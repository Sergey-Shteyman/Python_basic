from typing import Callable, Any
from functools import wraps
from time import sleep


def wait_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        for sec in range(3, 0, -1):
            print(f"Осталось ждать {sec} секунды...")
            sleep(1)
        result = func(*args, **kwargs)
        return result

    return wrapped_func


def loging(func=Callable) -> Callable:
    """
    Декоратор, логирующий работу кода
    """

    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        print(f"Вызывается функция: {func.__name__}\n"
              f"Позиционные аргументы: {args}\n"
              f"Именованные аргументы: {kwargs}")
        print("Функция успешно завершила работу!")
        return result

    return wrapped_func


@wait_time
@loging
def qube_number(number: int):
    """
    Выдает сумму кубов от 1 до введенного значения

    :return: сумма кубов
    """
    return sum([num**3 for num in range(1, number)])


qubes_summ = qube_number(10)
print(f"Сумма квадратов: {qubes_summ}")

