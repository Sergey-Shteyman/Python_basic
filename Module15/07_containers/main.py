quantity_containers = int(input("Введите колличество контейнеров: "))
lst_of_containers = []
for _ in range(1, quantity_containers + 1):
    print("Введите вес контейнера: ", end='')
    lst_of_containers.append(int(input()))
new_container = int(input("Введите вес нового контейнера: "))
for index in range(1, len(lst_of_containers) + 1):
    if lst_of_containers[index - 1] < new_container:
        print("Номер, куда встанет новый контейнер: ", index)
        break
