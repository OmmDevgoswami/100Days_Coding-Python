import os
def system_clean():
    if os.name == 'nt':
        os.system('cls')
        
LOGO = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(num1, num2):
    """ Adds two numbers together. """
    return (num1 + num2)

def sub(num1, num2):
    """ Subtract first number from second number. """
    return (num1 - num2)

def mul(num1, num2):
    """ Multiply two numbers together. """
    return (num1 * num2)

def div(num1, num2):
    """ Divide first number from second number. """
    if num2 != 0:
        return (num1 - num2)
    else:
        return ("Invalid")

def pow(num1, num2 = 2):
    """ 
    num_1 , num_2 times 
    By deafult : Generally used to find the Square of a number.
    """
    return (num1 ** num2)

cal_operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    "^" : pow
}

advance_operators = {
    
}

def calculator():
    print (LOGO)
    num_1 = float(input("Enter the First Number: "))
    for symbols in cal_operators:
        print(symbols)
    while True:
        symbol = input("Enter the Operation: ")
        num_2 = float(input("Enter the Next Number: "))
        answer = cal_operators[symbol](num_1, num_2)
        print (f"Result: {num_1} {symbol} {num_2} = {answer}")
        
        loop = input("Type 'y' to Continue or 'n' to restart. " ).lower()
        if loop == "n":
            system_clean()
            calculator ()
        elif loop == "y":
            num_1 = answer

calculator()