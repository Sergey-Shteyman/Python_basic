from typing import Callable


def decorator_with_args_for_any_decorator(func) -> Callable:
    """
    Декоратор функция, принимает от декорируемого декоратора аргументы, которые передали в декорируемый декоратор.
    :param func: Callable принимаемая декорируемая функция.
    :return: Callable возвращаем объект декорируемой функции
    """

    def wrapper(*args, **kwargs) -> Callable:
        """
        Декоратор функция обертка, принимает аргументы от декорируемой функции, и возвращает объекта декорируемой
        функции.
        :param args: *args принимает позиционные аргументы.
        :param kwargs: **kwargs принимает именованные аргументы.
        :return: Callable декорируемый декоратор
        """
        print('Переданные арги и кварги в декоратор: {args}, {kwargs}'.format(args=args, kwargs=kwargs))
        return func

    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable):
    """
    Декоратор функция, принимает объект функции
    :param func: Callable - объект декорируемая функция
    :return: Callable - объект декорируемая функция
    """

    def wrapper(*args, **kwargs) -> Callable:
        """
        Декоратор функция возвращает результат работы декорируемой функции.
        :param args: *args позиционные аргументы декорируемой функции.
        :param kwargs: **kwargs именованные аргументы декорируемой функции.
        :return:
        """
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей', 4564564, test_01=34, test_02='аргумент my_str')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
