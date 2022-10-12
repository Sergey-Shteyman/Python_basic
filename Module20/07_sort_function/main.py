def tpl_sort(collection):
    for number in collection:
        if not isinstance(number, int):
            return collection
    extra_collection = list(collection)
    return tuple(sorted(extra_collection))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
