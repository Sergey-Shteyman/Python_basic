from typing import Callable, Any
import functools
import time
from datetime import datetime


def timer(cls, func: Callable, day_formate: str) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        formate = day_formate
        for sym in formate:
            if sym.isalpha():
                formate = formate.replace(sym, '%' + sym)

        print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(formate)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
        return result

    return wrapped_func


def log_methods(formate: str) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его
    ко всем методам класса.
    """
    @functools.wraps(log_methods)
    def decorate(cls) -> Any:
        for i_method_name in dir(cls):
            if not i_method_name.startswith("__"):
                current_method = getattr(cls, i_method_name)
                decorated_method = timer(cls, current_method, formate)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate

@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
