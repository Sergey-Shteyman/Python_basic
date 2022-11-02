from typing import Any, Callable


def counter(func) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    func.__invocation_count__ = 0

    def wrapper(*args, **kwargs) -> Any:
        func.__invocation_count__ += 1
        result = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, func.__invocation_count__))
        return result

    return wrapper


@counter
def greeting():
    print("Hello world")


greeting()
greeting()
greeting()
greeting()
