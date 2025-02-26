import time

def delayer_prompter(function):     
    def wrapper():
        time.sleep(2)
        function()
        time.sleep(3)
        function()
    
    return wrapper
    
    
@delayer_prompter #Using decorater to delay the printing
def hello():
    print("Hello World")
    
@delayer_prompter
def goodMorning():
    print("Good Morning")
   
def sayGreetings():
    print("Greetings Programmers")
    
#When called without decorator
sayGreetings()

#When called with decorator
hello()
goodMorning()

#How the actual decorator works:
decorated_function = delayer_prompter(sayGreetings)
decorated_function()

#Double Function Call
delayer_prompter(sayGreetings)()