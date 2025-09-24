def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

if __name__ == "__main__":
    print("Калькулятор запущен!")
    result = add(5, 3)
    print(f"5 + 3 = {result}")
