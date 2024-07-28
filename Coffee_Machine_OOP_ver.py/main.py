from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

LOGO = '''
   ____         __   __               __  __               _      _              
  / ___| ___   / _| / _|  ___   ___  |  \/  |  __ _   ___ | |__  (_) _ __    ___ 
 | |    / _ \ | |_ | |_  / _ \ / _ \ | |\/| | / _` | / __|| '_ \ | || '_ \  / _ \ 
 | |___| (_) ||  _||  _||  __/|  __/ | |  | || (_| || (__ | | | || || | | ||  __/
  \____|\___/ |_|  |_|   \___| \___| |_|  |_| \__,_| \___||_| |_||_||_| |_| \___|
  
'''
print (LOGO)
print ("Welcome to Me, The Great O' Coffee Machine.")
menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
    
while True:
    print (f"What Would you like to get today? \n{menu.get_items()}")
    print ("'Report' of Resources.\nPress 'off' to Close the Coffee Machine.\n")
    choice  = input("Choose Your Today's Booster Drink: ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print ()
        coffee_maker.report()
        money.report()
        print ()
        print ("Ready for Another One ?")
    else:
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee):
            print (f"You choosed {choice}. It's Price is {coffee.cost}")
            if money.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
                print ()
                print ("Ready for Another One ?")
        else:
            break
        
print ("Thank You for Using Me !!\nIt's nice to help you brew some nice Coffee.")