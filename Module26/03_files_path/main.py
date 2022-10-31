import os


def files_path(core_path, folder_name):
    for i_elem in os.listdir(core_path):
        current_path = os.path.join(core_path, i_elem)
        if os.path.isdir(current_path) and i_elem != folder_name:
            yield from files_path(current_path, folder_name)
        elif os.path.isfile(current_path):
            yield os.path.join(current_path, i_elem)


folder_name = "Module26"
abs_core_path = os.path.abspath(os.path.join("..", "..", "Module26"))
result = files_path(abs_core_path, folder_name)
for path in result:
    print(path)
