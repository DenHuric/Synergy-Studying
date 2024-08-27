import collections

pets = {
  1: {
    "Мухтар": {
      "Вид питомца": "Собака",
      "Возраст питомца": 9,
      "Имя владельца": "Павел"
    },
  },
  2: {
    "Каа": {
      "Вид питомца": "желторотый питон",
      "Возраст питомца": 19,
      "Имя владельца": "Саша"
    },
  },
}

# Вспомогательные функции

def get_year_suffix(age_str):
    age = int(age_str)

    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"
    
def get_pet(id):
   if(id in pets):
      return pets[id]
   else:
      print("Питомец не найден")
      return False
   
def pets_list():
   print("Список питомцев:")
   for key in pets:
      print(pets[key])
# Базовые функции

def create(pet_name, pet_type, pet_age, pet_owner) :
  last_index = collections.deque(pets, maxlen=1)[0] + 1
  pets[last_index] = {
    pet_name: {
      "Вид питомца": pet_type,
      "Возраст питомца": pet_age,
      "Имя владельца": pet_owner
    }
  }

def read(id) :
   pet = get_pet(id)

   if(not pet):
      return False
   
   pet_name = list(pet.keys())[0]
   pet_type = pet[pet_name]['Вид питомца']
   pet_age = pet[pet_name]['Возраст питомца']
   pet_owner = pet[pet_name]['Имя владельца']
   year_suffix = get_year_suffix(pet[pet_name]['Возраст питомца'])
   print(f"Это {pet_type} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {year_suffix}. Имя владельца: {pet_owner}")
   return True

def update() :
   print("Список обновлен")

def delete(id) :
   pet = get_pet(id)

   if(not pet):
    return False
   
   del pets[id]
   print("Питомец удален")


command = ""

while command != 'stop':
  pets_list()
  print("Действие со списком (create, read, update, delete, stop):")
  command = input()

  if command == 'create':
    print("Введите имя питомца:")
    pet_name = input()
    print("Введите вид питомца:")
    pet_type = input()
    print("Введите возраст питомца:")
    pet_age = int(input())
    print("Введите имя хозяина:")
    pet_owner = input()
    create(pet_name, pet_type, pet_age, pet_owner)

  if command == 'read':
    print("Введите идентификатор питомца:")
    pet_id = int(input())
    read(pet_id)

  if command == 'update':
    update()

  if command == 'delete':
    print("Введите идентификатор питомца:")
    pet_id = int(input())
    delete(pet_id)