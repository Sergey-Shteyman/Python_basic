from statistics import mean


class Student:

    def __init__(self, fool_name, number_group, progress):
        self.fool_name = fool_name
        self.number_group = number_group
        self.progress = progress


students = [
    Student("Vlad Ivanov", 1, [4, 3, 2, 5, 5]),
    Student("Andrey Averin", 1, [3, 5, 3, 3, 3]),
    Student("Ivan Mirosh", 1, [2, 3, 4, 2, 2]),
    Student("Vanya Dobryi", 1, [2, 2, 2, 2, 2]),
    Student("Dobrinya Nikitich", 1, [2, 2, 2, 1, 5]),
    Student("Vanya Averin", 1, [3, 5, 1, 4, 5]),
    Student("Vlad Dobryi", 1, [2, 3, 3, 3, 3]),
    Student("Sergey Dobryi", 1, [2, 2, 2, 2, 2]),
    Student("Vanya Ivanov", 1, [1, 1, 1, 2, 5]),
    Student("Sergey Shteyman", 1, [4, 5, 5, 5, 5])
]


def students_progress(students):
    students.sort(key=sorted_by_middle_score, reverse=True)
    print("\nОтсортированный список по среднему баллу:\n")
    for student in students:
        middle_score = mean(student.progress)
        print(f"Средний балл студента {student.fool_name} "
              f"равен: {middle_score}")


def sorted_by_middle_score(student_progress):
    if isinstance(student_progress, Student):
        middle_score = mean(student_progress.progress)
        print(f"Средний балл студента {student_progress.fool_name} "
              f"равен: {middle_score}")
        return middle_score


students_progress(students)
