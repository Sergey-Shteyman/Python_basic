class Child:

    def __init__(self, name, age, behavior_state, hungry_state):
        self.name = name
        self.age = age
        self.behavior_state = behavior_state
        self.hungry_state = hungry_state

    def is_behavior_state(self):
        return self.behavior_state

    def is_hungry_state(self):
        return self.hungry_state