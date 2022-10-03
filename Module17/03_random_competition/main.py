import random

firs_command = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_command = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [
    firs_command[index] if firs_command[index] > second_command[index]
    else second_command[index] for index in range(20)
]

print(f"Первая команда: {firs_command}", end='\n')
print(f"Вторая команда: {second_command}", end='\n')
print(f"Победители тура: {winners}")
