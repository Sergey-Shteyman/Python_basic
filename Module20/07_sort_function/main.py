def sort_collection(collection):
    for number in collection:
        if not isinstance(number, int):
            return collection
    extra_collection = list(collection)
    return tuple(sorted(extra_collection))


print(sort_collection((6, 3, -1, 8, 4, 10, -5)))
