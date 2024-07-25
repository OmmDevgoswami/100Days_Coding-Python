LOGO = '''
   ____         __   __               __  __               _      _              
  / ___| ___   / _| / _|  ___   ___  |  \/  |  __ _   ___ | |__  (_) _ __    ___ 
 | |    / _ \ | |_ | |_  / _ \ / _ \ | |\/| | / _` | / __|| '_ \ | || '_ \  / _ \
 | |___| (_) ||  _||  _||  __/|  __/ | |  | || (_| || (__ | | | || || | | ||  __/
  \____|\___/ |_|  |_|   \___| \___| |_|  |_| \__,_| \___||_| |_||_||_| |_| \___|
'''


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

machine_money = 500

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def checkResources(item):
    for ingredient in MENU[item]["ingredients"]:
        if ((resources["water"] == 0) or (resources["milk"] == 0) or (resources["coffee"] == 0)):
            print (f"Insufficient Resources!!\nYour {item} Couldn't be prepared.")
        elif resources[ingredient] < MENU[item]["ingredients"][ingredient]:
            print (f"{ingredient} is available in insufficient amount.")
            print (f"Sorry, unable to prepare your {item}.")
        else:
            # print (f"Preparing your {item}...")
            money = 0
            print ("Almost Done !!")
            while True:
                print ("Please Insert the Required Money: ")
                bill_1 = int(input("10 X ")) or 0
                bill_2 = int(input("20 X ")) or 0
                bill_3 = int(input("50 X ")) or 0
                bill_4 = int(input("100 X ")) or 0
                bill_5 = int(input("200 X ")) or 0
                money = bill_1 + bill_2 + bill_3 + bill_4 + bill_5
                if (money < MENU[item]["cost"]):
                    print ("Sorry, you have entered the wrong amount. Please try again!!")
                    continue
                elif (money > MENU[item]["cost"]):
                    print (f"Ohh I See, You have entered an amount greater than your {item}")
                    print (f"Here's Your Change {machine_money - money}")
                    
                
                
            
            

print ("    MENU    ")
for i, n in enumerate(MENU) :
    print(f"{i+1} {n}")
coffee_choice = input("Choose Your Coffee: ")

checkResources(coffee_choice)
