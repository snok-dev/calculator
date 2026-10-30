"""A simple command-line calculator."""


def calculate(a, op, b):
    """Return the result of applying op to a and b, or an error message."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: can't divide by zero"
        return a / b
    else:
        return "Error: unknown operation"


def main():
    print("Simple Calculator")
    while True:
        first = input("First number (or 'q' to quit): ")
        if first == "q":
            print("Goodbye!")
            break
        op = input("Operation (+, -, *, /): ")
        second = input("Second number: ")

        try:
            result = calculate(float(first), op, float(second))
            print("Result:", result)
        except ValueError:
            print("Please enter valid numbers.")
        print()


if __name__ == "__main__":
    main()
