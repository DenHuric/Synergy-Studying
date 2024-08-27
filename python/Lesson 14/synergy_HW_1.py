

def write_list(list, i = 0):
  if(not i in range(len(list))):
    print("Конец списка")
    return True
  
  print(list[i])
  write_list(list, i + 1)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
write_list(list)