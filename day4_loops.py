n = int(input("Введи число: "))
if n % 2 == 0:
    print(f"Число {n} - Четное")
else:
    print(f"Число {n} - Нечетное")

# ==== Цикл While ====
print("\n=== Цикл while ===")
# Простой счетчик
i = 1
while i <= 5:
    print(f"Итерация {i}")
    i = i + 1

# Сумма чисел от 1 до N
print("\n=== Сумма чисел ===")
n = int(input("До какого числа считать сумму? "))
summa = 0
counter = 1
while counter <= n:
    summa = summa + counter
    counter = counter + 1
print(f"Сумма от 1 до {n} = {summa}")

# Выход из цикла через break
print("\n=== Выход из цикла ===")
while True:
    answer = input("Введи 'выход' чтобы остановиться: ")
    if answer == "Выход":
        print("Пока!")
        break
    else:
        print(f"Ты ввел: {answer}")

# ===== ЦИКЛ FOR =====
print("\n=== Цикл for ===")
# Перебор чисел от 1 до 5
for i in range(1,6):
    print(f"Число: {i}")

# Шаг 2
print("\n=== Шаг 2 ===")
for i in range(0,10,2):
    print(f"Четное: {i}")

 # Обратный отсчет
print("\n=== Обратный отсчет ===")
for i in range(5,0,-1):
    print(i)
print("Поехали!")

# Перебор строки
print("\n=== Перебор строки ===")
word = "Python"
for letter in word:
    print(f"Буква:{letter}")

# Сумма через for
print("\n=== Сумма через for ===")
n = int(input("До какого числа считать сумму? "))
summa = 0
for i in range(1,n + 1):
    summa = summa + i
print(f"Сумма от 1 до {n} = {summa}")

# ===== ЗАДАЧА 1: Таблица умножения на 5 =====
print("\n=== Задача 1 ===")
for i in range(1,11):
    print(f"5 x {i} = {5 * i}")

# ===== ЗАДАЧА 2: Факториал числа =====
print("\n=== Задача 2 ===")
n = int(input("Введи число: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(f"{n}! = {factorial}")

# ===== ЗАДАЧА 3: Четные числа от 1 до N =====
print("\n=== Задача 3 ===")
n = int(input("Введи N: "))
for i in range(2, n + 1, 2):
    print(i, end="")
print()

# ===== ЗАДАЧА 4: Угадай число (while) =====
print("\n=== Задача 4 ===")
secret = 7
guess = int(input("Угадай число от 1 до 10: "))
while guess != secret:
    print("Не угадал!")
    guess = int(input("Попробуй ещё: "))
print("Поздравляю! Ты угадал!")

# ===== ЗАДАЧА 5: Сумма только четных чисел от 1 до N =====
print("\n=== Задача 5 ===")
n = int(input("Введи N: "))
summa = 0
for i in range(2, n + 1, 2):
    summa = summa + i
print(f"Сумма четных от 1 до {n}: {summa}")

# ===== ЗАДАЧА 6: Обратный отсчет с вводом =====
print("\n=== Задача 6 ===")
start = int(input("С какого числа начать отсчет? "))
for i in range(start, 0, -1):
    print(i)
print("БУМ!")


