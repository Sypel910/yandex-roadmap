# ==== ЦЕЛЫЕ ЧИСЛА (int) ====
x = 10
y = 3
print("Целые числа")
print(f"{x} + {y} = {x + y}") # 13
print(f"{x} - {y} = {x - y}") # 7
print(f"{x} * {y} = {x * y}") # 30
print(f"{x} / {y} = {x / y}") # 3.333... (float)
print(f"{x} // {y} = {x // y}") # 3 (целочисленное деление)
print(f"{x} % {y} = {x % y}") # 1 (остаток)
print()
# ==== Дробные числа (float) ====
pi = 3.14159
radius = 5.0
area = pi * radius * radius
print(f"Площадь круга радиусом {radius}: {area}")
print()
# ==== Строки (str) ====
text = "Я учу Python"
print(text.upper()) # Я УЧУ PYTHON
print(text.lower()) # я учу python
print(len (text)) # 13 (длина строки)
# ==== Приведение типов ====
number_str = "42"
number_int = int(number_str)
print(number_int + 10) # 52
# Опасность: нельзя превратить буквы в число
# int("привет") # Ошибка!
# ==== Ввод от пользователя ====
user_input = input("Введи число: ")
user_number = int(user_input)
print(f"Квадрат: {user_number * user_number}")



