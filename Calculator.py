from Calculator_Art import logo

def add(n1, n2):
    """Returns the sum of two numbers 'n1' and 'n2'"""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference between two numbers 'n1' and 'n2'"""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers 'n1' and 'n2'"""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of two numbers 'n1' and 'n2'"""
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)
    num1 = float(input("First number:\n"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol_1 = input("Pick an operation from the line above:\n ")
    
        num2 = float(input("Next number\n"))
        calculation_function = operations[operation_symbol_1]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol_1} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
