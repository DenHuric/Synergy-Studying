import random

def generate_matrix(x, y):
  result = []
  for i in range(y):
    row = []
    for j in range(x):
      rand = random.randint(-100, 100)
      row.append(rand)
    result.append(row)
  return result

def sum_matrix(matrix1, matrix2):
  i = 0
  result = []
  matrix_length = len(matrix1)
  row_length = len(matrix1[0])

  while matrix_length > i:
    j = 0
    row = []
    while row_length > j:
      row.append(matrix1[i][j] + matrix2[i][j])
      j += 1
    result.append(row)
    i += 1

  return result


print("Введите x")
x = int(input())
print("Введите y")
y = int(input())

matrix1 = generate_matrix(x, y)
print(f"Первый сгенерированный массив: {matrix1}")
matrix2 = generate_matrix(x, y)
print(f"Второй сгенерированный массив: {matrix2}")
result_matrix = sum_matrix(matrix1, matrix2)
print(f"Результат суммирования: {result_matrix}")