
def calculate(number1, number2, operation):
    """
    Perform a mathematical operation on two numbers.
    """

    # Normalize the operation name
    operation = operation.strip().casefold()

    operations = {
        "addition": ("+", lambda a, b: a + b),
        "subtraction": ("-", lambda a, b: a - b),
        "multiplication": ("×", lambda a, b: a * b),
        "division": ("÷", lambda a, b: a / b),
    }

    # Check whether the operation exists
    if operation not in operations:
        raise ValueError("Invalid mathematical operation.")

    # Prevent division by zero
    if operation == "division" and number2 == 0:
        raise ValueError("Cannot divide by zero.")

    # Get the symbol and calculation function
    symbol, function = operations[operation]

    # Perform calculation
    result = function(number1, number2)

    return result, symbol
