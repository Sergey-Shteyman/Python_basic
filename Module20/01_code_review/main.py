students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_of_students(students):
    interests = []
    length_name = ""
    for id in students:
        interests.append(students[id]['interests'])
        length_name += students[id]['surname']
    return interests, len(length_name)


def pairs_id_age(students):
    pairs = []
    for id in students:
        pair = id, students[id]["age"]
        pairs.append(pair)
    return pairs


info_students = interests_of_students(students)
pairs = pairs_id_age(students)
interests = info_students[0]
lengt_names = info_students[1]
print(f"Список пар 'ID студента — возраст': {pairs}")
print(f"Полный список интересов всех студентов: {interests}")
print(f"\nОбщая длина всех фамилий студентов: {lengt_names}")
