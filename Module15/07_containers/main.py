quantity_containers = int(input("Введите колличество контейнеров: "))
list_of_containers = []
for i in range(1, quantity_containers + 1):
    print("Введите вес контейнера: ", end='')
    list_of_containers.append(int(input()))
new_container = int(input("Введите вес нового контейнера: "))
for i in range(1, len(list_of_containers) + 1):
    if list_of_containers[i - 1] < new_container:
        print("Номер, куда встанет новый контейнер: ", i)
        break
