print("Введите первый список, потом Enter и второй список")
# Ввод первого списка чисел
first_list = set()
while True:
    try:
        line = input()
        if line == "":
            break
        first_list.add(int(line))
    except EOFError:
        break

# Ввод второго списка чисел
second_list = set()
while True:
    try:
        line = input()
        if line == "":
            break
        second_list.add(int(line))
    except EOFError:
        break

# Находим пересечение двух множеств
common_elements = first_list & second_list

print("Кол-во общих элементов")
# Выводим количество общих элементов
print(len(common_elements))
