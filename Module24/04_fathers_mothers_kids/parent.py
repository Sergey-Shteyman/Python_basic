from child import Child

class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def info_parent(self):
        print(f"Имя родителя: {self.name}\n"
              f"Возраст родителя: {self.age}\n"
              f"Дети родителя: ")
        if isinstance(self.children, list):
            for child in self.children:
                print(f"{child.name}")
        print(" ")

    def quiet_child(self, child):
        if isinstance(child, Child):
            if not child.behavior_state:
                child.behavior_state = True

    def full_child(self, child):
        if isinstance(child, Child):
            if not child.hungry_state:
                child.hungry_state = True
