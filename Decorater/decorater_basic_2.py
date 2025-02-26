import time

def delayer_prompter():     
    print("I am a delay prompter")
    def wrapper():
        time.sleep(2)
        print("Helllo I am inside Wrapper function")
        time.sleep(3)
        print("Wahoo, the message gets printed after a while")
    
    return wrapper      #Here the function is returned not called{()-> is used to call a function}

delayer_prompter() #prints only "I am a delay prompter"

try:
    wrapper()           
except NameError as e:
    print(f"Error: {e}")
#This gives name error as wrapper() is a nested function and is present inside the delay_prompter(), hence it is not
#beyound the access of global scope.
print()
#Various ways to call a wrapper function are:
#1. Variable Call
wrapper = delayer_prompter()
wrapper() #prints all statements
print()

#2. Double Function Call
delayer_prompter()() #prints all statements
