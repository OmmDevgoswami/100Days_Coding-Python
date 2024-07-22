import random, os
def system_clean():
    if os.name == 'nt':
        os.system('cls')

LOGO = '''                                                                                                                                                                                                                                                            
                                                                                                         
  ,ad8888ba,                                                      888888888888  88                       
 d8"'    `"8b                                                          88       88                       
d8'                                                                    88       88                       
88             88       88   ,adPPYba,  ,adPPYba,  ,adPPYba,           88       88,dPPYba,    ,adPPYba,  
88      88888  88       88  a8P_____88  I8[    ""  I8[    ""           88       88P'    "8a  a8P_____88  
Y8,        88  88       88  8PP"""""""   `"Y8ba,    `"Y8ba,            88       88       88  8PP"""""""  
 Y8a.    .a88  "8a,   ,a88  "8b,   ,aa  aa    ]8I  aa    ]8I           88       88       88  "8b,   ,aa  
  `"Y88888P"    `"YbbdP'Y8   `"Ybbd8"'  `"YbbdP"'  `"YbbdP"'           88       88       88   `"Ybbd8"'  
                                                                                      
                                                                                    
            888b      88                                   88                                   
            8888b     88                                   88                                   
            88 `8b    88                                   88                                   
            88  `8b   88  88       88  88,dPYba,,adPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,  
            88   `8b  88  88       88  88P'   "88"    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
            88    `8b 88  88       88  88      88      88  88       d8  8PP"""""""  88          
            88     `8888  "8a,   ,a88  88      88      88  88b,   ,a8"  "8b,   ,aa  88          
            88      `888   `"YbbdP'Y8  88      88      88  8Y"Ybbd8"'    `"Ybbd8"'  88          
'''

def play_game():
    """" Run this to play the Game !! """
    print (LOGO)
    print ("Welcome to the Game !!\nTry to Guess a Randomly Generated Number Between '1' - '100' ")
    random_num = random.randint(1,100)
    difficulty = input("Choose Difficulty - Level:- 'Easy' or 'Hard' : ").lower()
    #Easy - difficulty
    if (difficulty == "easy"):
        print ("You have 10 attempts left")
        life = 10
        while (life != 0):
            guess = int(input("Guess the Number : "))
            if (guess == random_num):
                print ("Congratulations You Guessed the Right Number !!\nYou Won!!")
                break
            elif (random_num in range(guess, guess + 4)) or (random_num in range(guess - 3, guess + 1)):
                print ("You are Close!! Try Again !!")
                life -= 1;
                print (f"Attempt left are {life}")
            elif (guess > random_num ):
                print ("Too High !! Try Again !!")
                life -= 1;
                print (f"Attempt left are {life}")
            elif (guess < random_num ):
                print ("Too Low !! Try Again !!")
                life -= 1;
                print (f"Attempt left are {life}")
        if (life == 0):
            print ("You Lost!! Better Luck Next Time!!")
            if (input("Do you want to restart: ").lower() == "yes"):
                system_clean()
                play_game()
            else:
                print ("Thanks For Playing !!")
        else:
            print ("Thanks For Playing !!")
    #Hard - difficulty  
    elif (difficulty == "hard"):
        print ("You have 5 attempts left")
        life = 5
        while (life != 0):
            guess = int(input("Guess the Number : "))
            if (guess == random_num):
                print ("Congratulations You Guessed the Right Number !!\nYou Won!!")
                break
            elif (random_num in range(guess, guess + 2)) or (random_num in range(guess - 1, guess + 1)):
                print ("You are Close!! Try Again !!")
                life -= 1;
                print (f"Attempt left are {life}")
            elif (guess > random_num ):
                print ("Too High !! Try Again !!")
                life -= 1;
                print (f"Attempt left are {life}")
            elif (guess < random_num ):
                print ("Too Low !! Try Again !!")
                life -= 1;
                print (f"Attempt left are {life}")
        if (life == 0):
            print ("You Lost!! Better Luck Next Time!!")
            if (input("Do you want to restart: ").lower() == "yes"):
                system_clean()
                play_game()
            else:
                print ("Thanks For Playing !!")
        else:
            print ("Thanks For Playing !!")
            
play_game()