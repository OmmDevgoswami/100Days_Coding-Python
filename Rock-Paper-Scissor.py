rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
print ("Wlcome to the Rock-Paper-Scissor Python Game !!")
player = int (input ("Make a Choice:- 1.Rock, 2.Paper , 3.Scissor\n"))
computer = random.randint(1,3)
if (player == 1):
    print ("Player Chose: Rock")
    if (computer == 1):
        print ("Computer Chose: Rock")
        print ("This is a Tie !!")
    elif (computer == 2):
        print ("Computer Chose: Paper")
        print ("You Lose !!")
    else:
        print ("Computer Chose: Scissor")
        print ("You Win !!")
elif (player == 2):
    print ("Player Chose: Paper")
    if (computer == 2):
        print ("Computer Chose: Paper")
        print ("This is a Tie !!")
    elif (computer == 3):
        print ("Computer Chose: Scissor")
        print ("You Lose !!")
    else:
        print ("Computer Chose: Rock")
        print ("You Win !!")
elif (player == 3):
    print ("Player Chose: Scissor")
    if (computer == 3):
        print ("Computer Chose: Scissor")
        print ("This is a Tie !!")
    elif (computer == 1):
        print ("Computer Chose: Rock")
        print ("You Lose !!")
    else:
        print ("Computer Chose: Paper")
        print ("You Win !!")
else:
    print ("Invlaid Choice Entered !!")

