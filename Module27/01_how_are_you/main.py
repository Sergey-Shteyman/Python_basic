from typing import Callable, Any
import functools


def how_are_you(func=Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return result

    return wrapped_func


def loging(func=Callable) -> Callable:
    """
    Декоратор, логирующий работу кода
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        print(f"Вызывается функция: {func.__name__}\n"
              f"Позиционные аргументы: {args}\n"
              f"Именованные аргументы: {kwargs}")
        print("Функция успешно завершила работу!")
        return result

    return wrapped_func


@loging
@how_are_you
def qube_number(number: int):
    """
    Выдает сумму кубов от 1 до введенного значения

    :return: сумма кубов
    """
    return sum([num**3 for num in range(1, number)])


qubes_summ = qube_number(10)
print(f"Сумма квадратов: {qubes_summ}")
