# ==== Простое условие if ====
age = 18
if age >= 18:
    print("Ты совершенолетний!")

# ==== if-else (если-иначе) ====
age = 16
if age >= 18:
    print("Ты можешь водить машину")
else:
    print("Ещё рано, подожди")

# ==== if-elif-else (много вариантов) ====
score = 85
if score >= 90:
    print("Отлично! 5")
elif score >= 70:
    print("Хорошо! 4")
elif score >= 50:
    print("Удовлетворительно! 3")
else:
    print("Плохо! 2")

# ==== Логические операторы ====
age = 20
has_license = True
if age >= 18 and has_license:
    print("Ты можешь сесть за руль")
if age < 18 or age > 65:
    print("У тебя скидка на билет")
if not has_license:
    print("Нужно получить права")



# ==== Задача 1: Четное или нечетное ====
print("\n=== Задача 1 ===")
num = int(input("Введи число: "))
if num % 2 == 0:
    print(f"{num} - четное")
else:
    print(f"{num} - нечетное")

# ==== Задача 2: Максимум из двух чисел ====
print("\n=== Задача 2 ===")
a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))
if a > b:
    print(f"Максимум: {a}")
elif b > a:
    print(f"Максимум: {b}")
else:
    print("Числа равны")

# ==== Задача 3: Возрастная группа ====
print("\n=== Задача 3 ===")
age = int(input("Сколько тебе лет? "))
if age < 13:
    print("Ребенок")
elif age < 18:
    print("Подросток")
elif age < 60:
    print("Взрослый")
else:
    print("Пожилой")

# ==== Задача 4: Проверка пароля ====
print("\n=== Задача 4 ===")
password = input("Введи пароль: ")
if password == "yandex2026":
    print("Доступ разрешен!")
else:
    print("Доступ запрещен!")

# ===== ЗАДАЧА 5: Калькулятор =====
print("\n=== Задача 5 ===")
x = float(input("Первое число: "))
y = float(input("Второе число: "))
op = input("Операция (+, -, *, /): ")
if op == "+":
    print(f"{x} + {y} = {x + y}")
elif op == "-":
    print(f"{x} - {y} = {x - y}")
elif op == "*":
    print(f"{x} * {y} = {x * y}")
elif op == "/":
    if y != 0:
        print(f"{x} / {y} = {x / y}")
    else:
        print("Ошибка: деление на ноль")
else:
    print("Неизвестная операция")

# ===== ЗАДАЧА 6: Високосный год =====
print("\n=== Задача 6 ===")
year = int(input("Введи год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} — високосный")
else:
    print(f"{year} — не високосный")

# ==== Задача 7: Максимум из трех чисел ====
print("\n=== Задача 7 ===")
a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))
c = int(input("Введи третье число: "))
if a >= b and a >= c:
    print(f"Максимум: {a}")
elif b >= a and b >= c:
    print(f"Максимум: {b}")
else:
    print(f"Максимум: {c}")               

