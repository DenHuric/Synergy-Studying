print("Введите длинну списка:") 
N = int(input())
numbers = []

print("Введите числа через Enter")
for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers.reverse()

print()
print("Перевернутый массив:")
for num in numbers:
    print(num)
