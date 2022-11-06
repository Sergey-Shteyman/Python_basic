import itertools

password_combinations = itertools.product(range(10), repeat=4)

for password in password_combinations:
    print(password)
