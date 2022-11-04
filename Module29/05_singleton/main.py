def singleton(cls):
    _cls = None

    def wrapped_function():
        nonlocal _cls
        if _cls is None:
            _cls = cls()
        return _cls

    return wrapped_function


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
