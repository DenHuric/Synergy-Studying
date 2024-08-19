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

# Ввод данных
print("Введите вид питомца:")
pet_type = input()
print("Введите возраст питомца:")
pet_age = input()
print("Введите имя питомца:")
pet_name = input()

# Получаем окончание для возраста
year_suffix = get_year_suffix(pet_age)
print(f"Это {pet_type} по кличке \"{pet_name}\". Возраст: {pet_age} {year_suffix}.")
