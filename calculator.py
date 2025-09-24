<<<<<<< HEAD
def calculate(operation, a, b):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Unknown operation"

def main():
    print("Calculator started!")
    result = calculate('+', 10, 2)
    print(f"10 + 2 = {result}")

if __name__ == "__main__":
    main()
=======
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
>>>>>>> feature-calculation
