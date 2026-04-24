numbers = [10, 20, 30, 40, 50]
summa = 0
for num in numbers:
    summa = summa + num
print(f"Сумма: {summa}")

# ===== ЧТО ТАКОЕ СЛОВАРЬ? =====
print("\n=== Словари (dict) ===")
student = {
    "name": "Степан",
    "age": 16,
    "city": "Москва"
}
print(f"Студент: {student}")

# ===== ДОСТУП К ЗНАЧЕНИЯМ =====
print("\n=== Доступ к значениям ===")
print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")

# ===== ИЗМЕНЕНИЕ И ДОБАВЛЕНИЕ =====
print("\n=== Изменение и добавление ===")
student["age"] = 17
student["university"] = "НИУ ВШЭ"
print(f"После изменений: {student}")

# ===== МЕТОДЫ items(), keys(), values() =====
print("\n=== Методы ===")
print(f"Все пары: {list(student.items())}")
print(f"Все ключи: {list(student.keys())}")
print(f"Все значения: {list(student.values())}")

# ===== ПРОВЕРКА НАЛИЧИЯ КЛЮЧА =====
print("\n=== Проверка наличия ключа ===")
if "name" in student:
    print("Ключ 'name' есть в словаре")

# ===== МНОЖЕСТВА (SET) =====
print("\n=== Множества (set) ===")
numbers_set = {1, 2, 3, 3, 3, 4, 5}
print(f"Множество: {numbers_set}")

# Удаление дубликатов из списка
fruits = ["яблоко", "банан", "яблоко", "апельсин"]
unique = set(fruits)
print(f"Уникальные фрукты: {unique}")

# ===== ЗАДАЧА 1: Телефонная книга =====
print("\n=== Задача 1 ===")
phone_book = {
    "Анна": "89123456789",
    "Борис": "89234567890",
    "Виктор": "89345678901"
}
name = input("Введите имя: ")
if name in phone_book:
    print(f"Номер {name}: {phone_book[name]}")
else:
    print(f"{name} не найден")

# ===== ЗАДАЧА 2: Подсчет букв =====
print("\n=== Задача 2 ===")
text = input("Введите строку: ")
letter_count = {}
for letter in text:
    if letter in letter_count:
        letter_count[letter] = letter_count[letter] + 1
    else:
        letter_count[letter] = 1
print(f"Подсчет букв: {letter_count}")                    

# ===== ЗАДАЧА 3: Средний балл =====
print("\n=== Задача 3 ===")
grades = {
    "Математика": 5,
    "Физика": 4,
    "Информатика": 5,
    "Русский": 3
}
summa = 0
for subject in grades:
    summa = summa + grades[subject]
average = summa / len(grades) 
print(f"Средний балл: {average}")  

# ===== ЗАДАЧА 4: Объединение словарей =====
print("\n=== Задача 4 ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(f"Объединенный: {dict1}")

# ===== ЗАДАЧА 5: Удаление дубликатов =====
print("\n=== Задача 5 ===")
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
unique = list(set(numbers))
print(f"Без дубликатов: {unique}")

# ===== ЗАДАЧА 6: Инвертирование словаря =====
print("\n=== Задача 6 ===")
original = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in original.items():
    inverted[value] = key
print(f"Инвертированный: {inverted}")    