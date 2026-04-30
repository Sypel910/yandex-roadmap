# ===== ЗАПИСЬ В ФАЙЛ =====
print("\n=== Запись в файл ===")

with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Привет, Яндекс!\n")
    file.write("Я учусь работать с файлами.\n")

print("Файл test.txt создан")

# ===== ЧТЕНИЕ ИЗ ФАЙЛА =====
print("\n=== Чтение из файла ===")

with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(f"Содержимое:\n{content}")

# ===== ДОЗАПИСЬ В ФАЙЛ =====
print("\n=== Дозапись ===")

with open("test.txt", "a", encoding="utf-8") as file:
    file.write("Ещё одна строка\n")

with open("test.txt", "r", encoding="utf-8") as file:
    print(file.read())

# ===== РАБОТА С JSON =====
print("\n=== JSON ===")

import json

data = {
    "name": "Степан",
    "age": 16,
    "skills": ["Python", "Git", "VS Code"]
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("JSON записан в data.json")

with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(f"Загружено: {loaded_data}")

# ===== ЗАДАЧА 1: Сохранить список =====
print("\n=== Задача 1 ===")
def save_to_file(filename, lines):
    with open(filename, "w", encoding="utf-8") as file:
              for line in lines:
                file.write(line + "\n")
fruits = ["Яблоко", "Банан", "Апельсин", "Киви"]
save_to_file("fruits.txt", fruits)
print("Файл fruits.txt создан")

# ===== ЗАДАЧА 2: Прочитать файл =====
print("\n=== Задача 2 ===")
def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return[line.strip() for line in file.readlines()]
loaded = read_from_file("fruits.txt")
print(f"Прочитано: {loaded}") 

# ===== ЗАДАЧА 3: Подсчёт строк =====
print("\n=== Задача 3 ===")

def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return len(file.readlines())

print(f"Строк в fruits.txt: {count_lines('fruits.txt')}")

# ===== ЗАДАЧА 4: Копирование файла =====
print("\n=== Задача 4 ===")

def copy_file(src, dst):
    with open(src, "r", encoding="utf-8") as source:
        content = source.read()
    with open(dst, "w", encoding="utf-8") as dest:
        dest.write(content)

copy_file("fruits.txt", "fruits_copy.txt")
print("Файл fruits_copy.txt создан")

# ===== ЗАДАЧА 5: Поиск слова =====
print("\n=== Задача 5 ===")

def search_in_file(filename, word):
    with open(filename, "r", encoding="utf-8") as file:
        return word in file.read()

print(f"Слово 'апельсин': {search_in_file('fruits.txt', 'апельсин')}")
print(f"Слово 'ананас': {search_in_file('fruits.txt', 'ананас')}")
