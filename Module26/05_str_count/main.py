import os


def count_lines_of_code(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            len_code = 0
            if os.path.join(root, file).endswith(".py"):
                with open(os.path.join(root, file), "r") as current_file:
                    result = current_file.read().split('\n')
                    for line in result:
                        if len(line.strip()) == 0:
                            continue
                        elif line.strip()[0] == '#':
                            continue
                        elif line.strip()[0] == '"' or line.strip()[0] == "'":
                            continue
                        else:
                            len_code += 1
                    yield os.path.join(root, file), len_code


# 15 строчек
folder_name = "Module26"
folder_path = os.path.abspath(os.path.join("..", "..", folder_name))
result = count_lines_of_code(folder_path)
for path in result:
    print(f"{path[0]}   Строчек кода: {path[1]}")
