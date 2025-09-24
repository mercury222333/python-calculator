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
