print('''
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((        
      ''')
#Credits 'Unknown' Link : https://ascii.co.uk/art/swords
print ("\t\tWelcome to the Treausre Hunt Choice Game 'O Our Great Adventurer!!")
print ("Today's Quest : Find the Treasure Chest !!")
print ()
choice_1 = input("Oh it's a Fork Road Already !! Make a Decision: 'Left' or 'Right': ")
if (choice_1 == "Left"):
    print("You Proceed into your Gloryful path!! Oh no, there a River !!")
    choice_2 = input("Quick Make a Choice: 'Wait' for the Boat or 'Swim': ")
    if (choice_2 == "Wait" or "Boat"):
        print("You got on the Boat and you are now on the Mysterious Island!!\nThree Strange Doors Appear Infront of You: 'Red', 'Yellow' and 'Blue'")
        choice_3 = input("Make the Last Choice and have all the treasure: ")
        if (choice_3 == "Yellow"):
            print ("You got the Treasure!! You are now a Millionaire!!")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
                  ''')
            #Credits:'Tomekk'   Link:https://ascii.co.uk/art/treasure
        elif (choice_3 == "Red"):
            print ("Oh noooo!! You got burned by the Fire!!")
        elif (choice_3 == "Blue"):
            print ("Oh noooo!! You are attacked by Monsters!!\nGame Over")
        else:
            print ("Invalid Choice!!\nGame Over")
    elif(choice_2 == "Swim"):
        print ("Oh Noo!! You are Attacked By the Crocodiles!!\nGame Over!!")
    else:
         print ("Invalid Choice, Monsters Attacked You!!\nGame Over")
else:
    print ("Oh noo!! Bad Start, wild Bear is Chasing you!!\nGame Over.")
            
             