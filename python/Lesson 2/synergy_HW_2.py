number = input("Введите пятизначное целое число: ")

# Проверка, что число является пятизначным
if len(number) != 5 or not number.isdigit():
    print("Пожалуйста, введите корректное пятизначное число.")
else:
    number = int(number)
    
    # Извлечение цифр
    tens_of_thousands = number // 10000 % 10
    thousands = number // 1000 % 10
    hundreds = number // 100 % 10
    tens = number // 10 % 10
    ones = number % 10
    
    tens_power = tens ** ones
    result = tens_power * hundreds
    difference = tens_of_thousands - thousands
    
    final_result = result / difference
    print(f"Результат: {final_result:.1f}")