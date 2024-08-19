print("Введите число.")
input = int(input())

if input < 0 and input % 2 == 0:
  print("Отрицательное четное число.")
elif input > 0 and input % 2 == 0:
  print("Положительное четное число.")
elif input % 2 !=0:
  print("Число не является четным")
else:
  print("Нулевое число.")