# ===== ЧТО ТАКОЕ ФУНКЦИЯ? =====
print("\n=== Функции ===")

def say_hello():
    print("Привет, мир!")

say_hello()

# ===== ФУНКЦИИ С ПАРАМЕТРАМИ =====
print("\n=== Приветствие ===")

def greet(name):
    print(f"Привет, {name}!")

greet("Степан")

# ===== ФУНКЦИИ С return =====
print("\n=== Сумма ===")

def add(a, b):
    return a + b

print(f"5 + 3 = {add(5, 3)}")

# ===== ФУНКЦИЯ — квадрат числа =====
print("\n=== Квадрат ===")

def square(x):
    return x * x

print(f"Квадрат 4: {square(4)}")
print(f"Квадрат 7: {square(7)}")

# ===== ФУНКЦИЯ — максимум из двух =====
print("\n=== Максимум ===")

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print(f"Максимум 10 и 20: {max_of_two(10, 20)}")

# ===== ФУНКЦИЯ — чётное или нечётное =====
print("\n=== Чётность ===")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(f"4 чётное? {is_even(4)}")
print(f"7 чётное? {is_even(7)}")

# ===== ФУНКЦИЯ — сумма списка =====
print("\n=== Сумма списка ===")

def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

my_numbers = [10, 20, 30, 40, 50]
print(f"Сумма {my_numbers}: {sum_list(my_numbers)}")

# ===== ФУНКЦИЯ — факториал =====
print("\n=== Факториал ===")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(f"5! = {factorial(5)}")   # 120
print(f"7! = {factorial(7)}")   # 5040

# ===== ФУНКЦИЯ — проверка простого числа =====
print("\n=== Простое число ===")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(f"7 простое? {is_prime(7)}")
print(f"10 простое? {is_prime(10)}")