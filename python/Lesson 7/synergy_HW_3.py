# Вводим последовательность чисел
sequence = input().split()

# Создаем пустое множество для отслеживания уже встреченных чисел
seen_numbers = set()

# Проходим по каждому числу в последовательности
for number in sequence:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)
