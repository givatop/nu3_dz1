list_len = int(input("Введите количество элементов: "))

user_list = [int(input(f"Введите {i} элемент: ")) for (i, _) in enumerate(range(list_len), start=1)]

user_list.sort()

print(user_list)
