import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise Exception("Cannot divide by zero!")
    return x / y

def main():
    while True:
        print("Select an operator:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        op = input("Enter your choice number: ")

        x = 0
        y = 0

        try:
            x = float(input("Enter your first number: "))
            y = float(input("Enter your second number: "))
        except ValueError:
            print("Please enter a number!")
            continue

        try:
            print("Answer:")
            match op:
                case "1":
                    print(add(x, y))
                case "2":
                    print(subtract(x, y))
                case "3":
                    print(multiply(x, y))
                case "4":
                    print(divide(x, y))
                case _:
                    print("Goodbye!")
                    break
        except Exception as e:
            logStdErr(e)

def logStdErr(msg):
    print("\n", file=sys.stderr)
    print(msg, file=sys.stderr)

if __name__ == '__main__':
    main()