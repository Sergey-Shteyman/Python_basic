import person
from random import randint, choice


def base_employee():
    name = choice(["Vlad", "Sergey",
                   "Nikita", "Arkadii",
                   "Artem", "Oleg",
                   "Ulukbek", "Hasanderbek"])
    sur_name = choice(["Shteyman", "Ivanov",
                       "Katanov", "Averin",
                       "Davidov", "Mesnyakov",
                       "Burduk", "Runduk"])
    age = randint(16, 60)
    return name, sur_name, age


def create_employee():
    employee = list()
    for _ in range(3):
        employee.append(person.Manager(*base_employee()))
    for _ in range(3):
        agent = person.Agent(*base_employee())
        agent.sales_amount = randint(100, 1000)
        employee.append(agent)
    for _ in range(3):
        worker = person.Worker(*base_employee())
        worker.work_hour = randint(5, 30)
        employee.append(worker)
    info_employee(employee)


def info_employee(employee):
    for person in employee:
        print(f"{person}")


create_employee()
