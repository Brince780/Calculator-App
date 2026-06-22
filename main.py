def add(n1, n2):
    """Adds the second value to the fists one"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts the second value from the first one"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies the second value with the first one"""
    return n1 * n2

def divide(n1, n2):
    """Divides the second value from the first one"""
    return n1 / n2

def calculator():
    print(logo)
    should_accumulate = True
    n1 = float(input("What is the first number: "))

    while should_accumulate:
        for keys in operations:
            print(keys)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What is the next number: "))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 30)
            calculator()

logo = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }
calculator()
