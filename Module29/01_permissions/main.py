import functools
from typing import Callable, Any


def check_permission(permission: str) -> Callable:
    """
    Декоратор, который проверяет
    есть ли у пользователя доступ
    к вызываемой функции
    """
    def access_level(func: Callable) -> Callable:
        user_permissions = ['admin']

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            try:
                if permission in user_permissions:
                    result = func(*args, *kwargs)
                    return result
                else:
                    raise PermissionError
            except PermissionError as error:
                print(f"PermissionError: У пользователя недостаточно прав, "
                      f"чтобы выполнить функцию {func.__name__}")

        return wrapped_func
    return access_level


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
