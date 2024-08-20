A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A % 2 != 0:
    A += 1

for num in range(A, B + 1, 2):
    print(num, end=' ')
