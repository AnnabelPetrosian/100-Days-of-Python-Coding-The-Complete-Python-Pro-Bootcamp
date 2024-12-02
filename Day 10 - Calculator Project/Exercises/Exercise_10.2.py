

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

number1 = int(input("What is the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from above: ")

number2 = int(input("What is the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(number1, number2)

print(f"{number1} {operation_symbol} {number2} = {answer}")


operation_symbol = input("Pick another operation: ")
number3 = int(input("What is the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(answer, number3)

print(f"{answer} {operation_symbol} {number3} = {second_answer}")