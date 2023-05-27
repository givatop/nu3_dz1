delimiters = (',', '.', '/')
delimiter_used = False

user_input = input("Введите элементы списка через один из символов "
                   "[\",\" \".\" \"/\"]: ")


for delimiter in delimiters:

    if delimiter not in user_input:
        continue

    if delimiter_used:
        raise ValueError("Нельзя использовать несколько разделителей")

    delimiter_used = True
    numbers = user_input.split(delimiter)
    numbers = set(numbers)

    print(numbers)
