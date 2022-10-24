import os


def files_and_folders(path):
    total_size = 0
    path, dirs, files = next(os.walk(path))
    for f in files:
        fp = os.path.join(path, f)
        total_size += os.path.getsize(fp)
    print('Размер каталога (в Кб): ', total_size / 1024)
    print('Количество подкаталогов: ', len(dirs))
    print('Количество файлов: ', len(files))


abs_path = os.path.abspath(os.path.join('..', '..', '..', "SkillBox"))
for i_elem in os.listdir(abs_path):
    print(i_elem)
files_and_folders(abs_path)
