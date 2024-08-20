print("Введите целое число:")
x = int(input())
zero = 0

for i in range(x):
  print("Введите целое число №",i + 1)
  n = int(input())
  if n == 0: 
    zero +=1

print("Количество нулей:", zero)