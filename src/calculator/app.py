from calculator.operations import add, subtract, multiply, divide

OPS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

def parse_number(text: str) -> float:
    return float(text)

def repl() -> None:
    print("Interactive Calculator (type 'quit' to exit)")
    print("Available operations:", ", ".join(OPS.keys()))

    while True:
        op = input("\nOperation (add/subtract/multiply/divide): ").strip().lower()

        if op in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        if op not in OPS:
            print("Invalid operation. Try again.")
            continue

        try:
            a = parse_number(input("Enter first number: ").strip())
            b = parse_number(input("Enter second number: ").strip())
            result = OPS[op](a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid number entered. Please enter numeric values.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()