class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f"Сотрудник: {self.__name} {self.__surname}\n"\
               f"Возраст: {self.__age}"


class Employee(Person):
    def calculate_salary(self):
        pass

    def __str__(self):
        return super().__str__() + f"\nЗарплата: {self.calculate_salary()}\n"


class Manager(Employee):
    __salary = 13000

    def calculate_salary(self):
        return self.__salary


class Agent(Employee):
    __salary = 5000
    sales_amount: int

    def calculate_salary(self):
        return round(self.__salary + (self.__salary * (5 / self.sales_amount)), 2)


class Worker(Employee):
    __salary_pro_hour = 100
    work_hour: int

    def calculate_salary(self):
        return self.__salary_pro_hour * self.work_hour
