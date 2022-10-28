from parent import Parent
from child import Child


def child_states(child):
    if isinstance(child, Child):
        if child.hungry_state:
            print(f"Ребенок по имени {child.name} сытый")
        else:
            print(f"Ребенок по имени {child.name} голодный")
            print("Покормите ребенка!\n")
        if child.behavior_state:
            print(f"Ребенок по имени {child.name} спокоен")
        else:
            print(f"Ребенок по имени {child.name} расстроен")
            print("Успокойте ребенка!\n")


first_child = Child("Sergey Shteyman", 23, True, False)
second_child = Child("Anastasia Shteyman", 38, False, True)

first_parant = Parent("Andrey Shteyman", 60, [first_child, second_child])
for child in first_parant.children:
    if first_parant.age - child.age < 16:
        print(f"Ребенок {child.name} не может быть ражден от родителя {first_parant.name}")
        if isinstance(first_parant.children, list):
            first_parant.children.pop(first_parant.children.index(child))
first_parant.info_parent()
child_states(first_child)
first_parant.full_child(first_child)
child_states(second_child)
first_parant.quiet_child(second_child)
child_states(second_child)




