from typing import Callable, Any


def debug(func: Callable) -> Callable:

    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        info_function = [repr(item) for item in args]
        info_function.extend([f'{key}={repr(value)}' for key, value in kwargs.items()])
        print(f"Вызывается {func.__name__}({', '.join(info_function)})")
        if args:
            print(f"'{func.__name__}' вернула значение '{func(*args, **kwargs)}'", end=' ')
        return result

    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return f"Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!"
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том", age=20)

