import os, math
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

#Basic Operations
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

def sqrt(num1, num2 = 2):
    """ 
    Squareroot of num_1 by num_2 
    By deafult : Generally used to find the Square-Root/UnderRoot of a number.
    """
    return (num1 ** (1/num2))

def percentage (num1, num2):
    """" Used to find the percentage of a number """
    return (num1 * (num2/100))

#Angular Convertion
def deg_to_rad(num):
    """" Used to convert Degrees to Radians """
    return math.radians(num)

def rad_to_deg(num):
    """" Used to convert Radians to Degrees """
    return math.degrees(num)

#Trigonometric Operations
def sin(num):
    """"
    Used to find the Sine of a number 
    By default use radian as the value. 
    """
    return math.sin(num)

def cos(num):
    """" 
    Used to find the Cosine of a number 
    By default use radian as the value. 
    """
    return math.cos(num)

def tan(num):
    """"
    Used to find the Tangent of a number  
    By default use radian as the value. 
    """
    return math.tan(num)

def cosec(num):
    """"
    Used to find the arc sine of a number
    By default use radian as the value.  
    """
    return math.asin(num)

def sec(num):
    """" 
    Used to find the arc cosine of a number  
    By default use radian as the value.
    """
    return math.acos(num)

def cot(num):
    """"
    Used to find the arc tangent of a number  
    By default use radian as the value. 
    """
    return math.atan2(num)

#Other Operations
def fact(num):
    """" Used to find the factorial of a number  """
    return math.gamma(num+1)
    # Gamme function is a more wide-use version of original Factorial function.


cal_operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    "^" : pow,
    "sqrt" : sqrt,
    "%" : percentage
}

adv_cal_operators = {
    "fact" : fact,
    "sin" : sin,
    "cos" : cos,
    "tan" : tan,
    "cosec" : cosec,
    "sec" : sec,
    "cot" : cot,
    "rad" : deg_to_rad,
    "deg" : rad_to_deg
}

def calculator():
    print (LOGO)
    choice = input("Choose 'Basic' or 'Advance' Calculator: ").lower()
    if (choice == "basic"):
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
    elif (choice == "advance"):
        for symbols in adv_cal_operators:
            print(symbols)
        while True:
            symbol = input("Enter the Operation: ")
            num = float(input("Enter the Number: "))
            answer = adv_cal_operators[symbol](num)
            print (f"Result: {symbol} ({num}) = {answer}")
            
            loop = input("Type 'y' to Continue or 'n' to restart. " ).lower()
            if loop == "n":
                system_clean()
                calculator ()      

calculator()