def singleton(cls):
    _cls = None

    def wrapped_function():
        nonlocal _cls
        if _cls is None:
            _cls = cls()
        return _cls

    return wrapped_function

