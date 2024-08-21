def get_year_suffix(age_str):
    # Преобразуем строку в целое число
    age = int(age_str)
    
    # Определение правильного окончания
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

pets = {}

# Ввод данных
print("Введите имя питомца:")
pet_name = input()
print("Введите вид питомца:")
pet_type = input()
print("Введите возраст питомца:")
pet_age = int(input())
print("Введите имя хозяина:")
pet_owner = input()

pets = {
    pet_name: {
        'pet_type' : pet_type,
        'pet_age' : pet_age,
        'pet_owner' : pet_owner
    }
}

# Получаем окончание для возраста
year_suffix = get_year_suffix(pets[pet_name]['pet_age'])
# Форматируем вывод
print(f"Это {pets[pet_name]['pet_type']} по кличке \"{pet_name}\". Возраст: {pets[pet_name]['pet_age']} {year_suffix}. Владелец: {pets[pet_name]['pet_owner']}")
