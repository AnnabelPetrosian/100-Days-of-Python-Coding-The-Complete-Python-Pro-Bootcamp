

# Calculator

# Add +
def add(x1, x2):
    return x1 + x2


# Subtract -
def subtract(x1, x2):
    return x1 - x2


# Multiply *
def multiply(x1, x2):
    return x1 * x2


# Divide /
def divide(x1, x2):
    return x1 / x2


operations = {"+": add,
              "-":subtract,
              "*": multiply,
              "/": divide}


def calculator():
    number1 = int(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number2 = int(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(number1, number2)

        print(f"{number1} {operation_symbol} {number2} = {answer}")

        if input(f"Type 'y' continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            number1 = answer
        else:
            should_continue = False
            calculator()


calculator()