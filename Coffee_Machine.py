import os
def systeam_clean():
    if os.name == 'nt':
        os.system('cls')

LOGO = '''
   ____         __   __               __  __               _      _              
  / ___| ___   / _| / _|  ___   ___  |  \/  |  __ _   ___ | |__  (_) _ __    ___ 
 | |    / _ \ | |_ | |_  / _ \ / _ \ | |\/| | / _` | / __|| '_ \ | || '_ \  / _ \ 
 | |___| (_) ||  _||  _||  __/|  __/ | |  | || (_| || (__ | | | || || | | ||  __/
  \____|\___/ |_|  |_|   \___| \___| |_|  |_| \__,_| \___||_| |_||_||_| |_| \___|
  
'''
print (LOGO)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0
        },
        "cost": 120,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    """ Used to display the resources left. """
    for items in resources:
        print (f"{items} : {resources[items]}")
    print()
    

def addResources():
    """ Add more resources to the Storage so more Coffee can be brewed """
    print ("Adding more resources....")
    for item in resources:
        if (item == "water"):
            resources[item] += 200
        elif (item == "milk"):
            resources[item] += 100
        elif (item == "coffee"):
            resources[item] += 50
        elif (item == "money"):
            continue
    print ("More Resources Added !!")
    print ()


def prepareCoffee(item):
    """ Main Function used to Create Coffee """
    loop_breaker = True
    for ingredient in MENU[item]["ingredients"]:
        if ((resources["water"] == 0) or (resources["milk"] == 0) or (resources["coffee"] == 0)):
            print (f"Insufficient Resources!!\nYour {item} Couldn't be prepared.")
        elif resources[ingredient] < MENU[item]["ingredients"][ingredient]:
            print (f"{ingredient} is available in insufficient amount.")
            print (f"Sorry, unable to prepare your {item}.")
        else:
            money = 0
            while loop_breaker:
                print ("Almost Done !!")
                print ("Please Insert the Required Money: ")
                print ("[#Leave the bills not used as empty field.]")
                bill_1 = input("10  X ") or 0
                bill_2 = input("20  X ") or 0
                bill_3 = input("50  X ") or 0
                bill_4 = input("100 X ") or 0
                bill_5 = input("200 X ") or 0
                money = int(bill_1)*10 + int(bill_2)*20 + int(bill_3)*50 + int(bill_4)*100 + int(bill_5)*200
                if (money < MENU[item]["cost"]):
                    print (f"Sorry, you have entered the wrong amount.\nReturning you {money} Please try again!!")
                    continue
                elif (money > MENU[item]["cost"]):
                    print (f"Ohh I See, You have entered an amount greater than your {item}")
                    print (f"Here's Your Change {money - MENU[item]['cost']}")
                    print (f"Preparing your {item}...")
                    print (f"Thanks for the wait !! Here's Your {item}\nHave a Nice Day Ahead !!")
                    print ()
                    for items in resources:
                        if (items == "water"):
                            resources[items] -= MENU[item]["ingredients"]['water']
                        elif (items == "milk"):
                            resources[items] -= MENU[item]["ingredients"]['milk']
                        elif (items == "coffee"):
                            resources[items] -= MENU[item]["ingredients"]['coffee']
                        elif (items == "money"):
                            resources[items] += MENU[item]["cost"]
                    loop_breaker = False
                elif (money == MENU[item]["cost"]):
                    print (f"Preparing your {item}...")
                    print (f"Thanks for the wait !! Here's Your {item}\nHave a Nice Day Ahead !!")
                    print ()
                    for items in resources:
                        if (items == "water"):
                            resources[items] -= MENU[item]["ingredients"]['water']
                        elif (items == "milk"):
                            resources[items] -= MENU[item]["ingredients"]['milk']
                        elif (items == "coffee"):
                            resources[items] -= MENU[item]["ingredients"]['coffee']
                        elif (items == "money"):
                            resources[items] += MENU[item]["cost"]
                    loop_breaker = False
          
                    
while True:                    
    print ("    MENU    ")
    for i, n in enumerate(MENU) :
        print(f"{i+1} {n}")
    print ("4 'Report' of Resources Left." )
    print ("5 Press 'off' to Stop the Machine." )
    
    coffee_choice = input("Choose Your Coffee ☕: ").lower()
    if (coffee_choice == "espresso") or (coffee_choice == "cappuccino") or (coffee_choice == "latte"):
        print (f"Your {coffee_choice} will cost {MENU[coffee_choice]['cost']}.")
        prepareCoffee(coffee_choice)
    elif (coffee_choice == "report"):
        resource = input("Do You wish to 'Add' resources or 'View' resources: ").lower()
        if (resource == "add"):
            addResources()
        elif (resource == "view"):
            report()
    elif (coffee_choice == "off"):
        break
systeam_clean()
print ("Thank You for Using Me !!\nIt's nice to help you brew some nice Coffee.")