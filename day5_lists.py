# ==== Создание списков ====
print("\n=== Создание списков ===")
numbers = [10, 20, 30, 40, 50]   
friends = ["Анна", "Борис", "Виктор"]
print(f"Список чисел: {numbers}")
print(f"Друзья: {friends}")

# ==== Доступ к элементам ====
print("\n=== Доступ к элементам ===")
print(f"Первый элемент: {numbers[0]}")
print(f"Последний элемент: {numbers[-1]}")

# ==== Изменение элементов ====
print("\n=== Изменение элементов ===")
numbers[2] = 99
print(f"После изменения: {numbers}")

# ==== Методы списков ====
print("\n=== Методы списков ===")
fruits = ["Яблоко", "Банан"]
fruits.append("Апельсин")
print(f"append: {fruits}")
fruits.insert(1, "Киви")
print(f"insert: {fruits}")
fruits.remove("Банан")
print(f"remove: {fruits}")

# ==== Перебор списка ====
print("\n=== Перебор списка ===")
for fruit in fruits:
    print(f"Фрукт: {fruit}")

# ===== ЗАДАЧА 1: Сумма чисел в списке =====
print("\n=== Задача 1 ===")
numbers = [5, 10, 15, 20, 25]  
summa = 0
for num in numbers:
    summa = summa + num
print(f"Сумма: {summa}")

# ===== ЗАДАЧА 2: Максимум в списке =====
print("\n=== Задача 2 ===")
numbers = [12, 45, 7, 89, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Максимум: {max_num}")

# ===== ЗАДАЧА 3: Список от 1 до N =====
print("\n=== Задача 3 ===")
n=int(input("Введи N: "))
numbers = []
for i in range(1, n + 1):
    numbers.append(i)
print(f"Список: {numbers}")    

# ===== ЗАДАЧА 4: Четные числа =====
print("\n=== Задача 4 ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print(f"Четные: {even}")

# ===== ЗАДАЧА 5: Умножить на 2 =====
print("\n=== Задача 5 ===")
numbers = [3, 6, 9, 12]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(f"Умноженный: {numbers}")

# ===== ЗАДАЧА 6: Поиск элемента =====
print("\n=== Задача 6 ===")
numbers = [10, 20, 30, 40, 50]
search = int(input("Какое число ищем? "))
found = -1
for i in range(len(numbers)):
    if numbers[i] == search:
        found = i
        break
if found != -1:
    print(f"Найдено на позиции {found}")
else:
    print("Не найдено")