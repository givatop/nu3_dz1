delimiter = ','


user_input = input("Введите элементы 1-го списка через запятую: ")
initial_numbers = user_input.split(delimiter)

user_input = input("Введите элементы 2-го списка через запятую: ")
deleting_numbers = user_input.split(delimiter)

for num in deleting_numbers:
    if num in initial_numbers:
        initial_numbers.remove(num)

print(initial_numbers)
