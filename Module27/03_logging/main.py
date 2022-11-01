from typing import Callable, Any
from datetime import datetime


def loging(func=Callable) -> Callable:
    """ Декоратор, логирующий работу кода """

    def wrapped_func(*args, **kwargs) -> Any:
        print(f"Вызывается функция: {func.__name__}\n"
              f"{func.__doc__}\n"
              f"Позиционные аргументы: {args}\n"
              f"Именованные аргументы: {kwargs}\n")
        try:
            result = func(*args, **kwargs)
            print("Функция успешно завершила работу!")
            return result
        except BaseException as error:
            handle_error(error)

    def handle_error(error):
        function_errors = "function_errors.log"
        current_time = datetime.now()
        time_error = f"{current_time.strftime('%d-%m-%Y %H:%M')} {current_time.second} seconds"
        time_error += f" {current_time.microsecond} microseconds"
        with open(function_errors, "a", encoding='utf-8') as error_file:
            error_file.write(f"Function name: {func.__name__}\n")
            error_file.write(f"Function doc: {func.__doc__}\n")
            error_file.write(f"Function error: {str(error)}\n")
            error_file.write(f"{time_error}\n")
            error_file.write(f"\n")

    return wrapped_func


@loging
def index_error():
    """Функция возвращает IndexError"""
    raise IndexError("IndexError")


@loging
def stop_iteration():
    """Функция возвращает StopIteration"""
    raise StopIteration("StopIteration")


@loging
def zero_division():
    """Функция возвращает ZeroDivisionError """
    raise ZeroDivisionError("ZeroDivisionError")


@loging
def value_error():
    """Функция возвращает ValueError """
    raise ValueError("ValueError")


@loging
def qube_number(number: int):
    """
    Выдает сумму кубов от 1 до введенного значения

    :return: сумма кубов
    """
    sum_cubes = sum([num ** 3 for num in range(1, number)])
    print(f"Сумма кубов: {sum_cubes}")
    return sum_cubes


index_error()
stop_iteration()
zero_division()
value_error()
qube_number(number=10)
