import os
def clear_screen():
  if os.name == 'nt':
    os.system('cls')
    
LOGO_1 = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                             
                       .-------------.
                      /_______________\\
'''

LOGO_2 = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print (LOGO_1)
print ("Welcome to the Silent/Blind Auction !!")
print ("Today with your Host - Me")
print ()

def maxBid(dict):
    max = 0
    winner = ""
    for key in dict:
        if int(dict[key]) > max:
            max = dict[key]
            winner = key
    print ()
    print (f"Congratulations !! The Highest bidding is ${max} by Tycoon {winner}.")
    print (f"{winner} takes it All \nThanks for Attending the Blind-Auction.")

Bidder_Record = {}
while True:
    Bidder_name = input("Please enter the Name of the Bidder: ")
    Bidding_amount = int(input("Enter the Bidding Amount: $"))
    Bidder_Record[Bidder_name] = Bidding_amount
    loop = input("Are there any more Bidders ?  Type 'yes' or 'no': ").lower()
    if loop == "no":
        clear_screen()
        print (LOGO_2)
        maxBid(Bidder_Record)
        break
    elif loop == "yes":
        clear_screen()