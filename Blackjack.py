import random, os
def system_clean():
    if os.name == 'nt':
        os.system('cls')

LOGO = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/  
'''
#print(LOGO)
cards = {
    0 : 11,
    1 : 2,
    2 : 3,
    3 : 4,
    4 : 5,
    5 : 6,
    6 : 7,
    7 : 8,
    8 : 9,
    9 : 10,
    10 : 10,
    11 : 10,
    12 : 10
}

def draw_cards(game = "n" , player_score = 0, computer_score = 0):
    symbol = ["♠", "♦", "♥", "♣️"]
    icon = random.choice(symbol)
    Cards_art = [
f'''
{ 'Ace' }
 -------------    
|A{icon}           |        
|   -------   |           
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |   {icon}   |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|   -------   | 
|           {icon}A| 
 -------------  
 ''',   
 f'''
 { '2' }
 -------------  
|2{icon}           | 
|   -------   | 
|  |       |  | 
|  |   {icon}   |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |   {icon}   |  | 
|  |       |  | 
|   -------   | 
|           {icon}2| 
 -------------  
 ''',  
f'''
{ '3' }
 -------------  
|3{icon}           | 
|   -------   | 
|  |       |  | 
|  |   {icon}   |  | 
|  |       |  | 
|  |   {icon}   |  | 
|  |       |  | 
|  |   {icon}   |  | 
|  |       |  | 
|   -------   | 
|           {icon}3| 
 -------------  
 ''', 
f'''
{ '4' }
 -------------  
|4{icon}           | 
|   -------   | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|   -------   | 
|           {icon}4| 
 -------------  
 ''',  f'''
 { '5' }
 -------------  
|5{icon}           | 
|   -------   | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |       |  | 
|  |   {icon}   |  | 
|  |       |  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|   -------   | 
|           {icon}5| 
 -------------  
 ''', 
 f'''
 { '6' }
 -------------  
|6{icon}           | 
|   -------   | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|   -------   | 
|           {icon}6| 
 -------------  
 ''', 
  f'''
  { '7' }
 -------------  
|7{icon}           | 
|   -------   | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |       |  | 
|  |{icon}  {icon}  {icon}|  | 
|  |       |  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|   -------   | 
|           {icon}7| 
 -------------  
 ''',
  f'''
  { '8' }
 -------------  
|8{icon}           | 
|   -------   | 
|  |{icon}     {icon}|  | 
|  |   {icon}   |  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |   {icon}   |  | 
|  |{icon}     {icon}|  | 
|   -------   | 
|           {icon}8| 
 -------------  
 ''',
 f'''
 { '9' }
 -------------  
|9{icon}           | 
|   -------   | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|  |   {icon}   |  | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|   -------   | 
|           {icon}9| 
 -------------  
 ''',  
 f'''
 { '10' }
 -------------  
|10{icon}          | 
|   -------   | 
|  |{icon}     {icon}|  | 
|  |   {icon}   |  | 
|  |{icon}     {icon}|  | 
|  |       |  | 
|  |{icon}     {icon}|  | 
|  |   {icon}   |  | 
|  |{icon}     {icon}|  | 
|   -------   | 
|          {icon}10| 
 -------------  
 ''',
 f'''
 { 'Jack' }
 -------------  
|J{icon}           | 
|   -------   | 
|  |{icon}      |  | 
|  |       |  | 
|  |       |  | 
|  |   J   |  | 
|  |       |  | 
|  |       |  | 
|  |      {icon}|  | 
|   -------   | 
|           {icon}J| 
 -------------  
 ''',
 f'''
 { 'Queen' }
 -------------  
|Q{icon}           | 
|   -------   | 
|  |{icon}      |  | 
|  |       |  | 
|  |       |  | 
|  |   Q   |  | 
|  |       |  | 
|  |       |  | 
|  |      {icon}|  | 
|   -------   | 
|           {icon}Q| 
 -------------  
 ''',
 f'''
 { 'King' }
 -------------  
|K{icon}           | 
|   -------   | 
|  |{icon}      |  | 
|  |       |  | 
|  |       |  | 
|  |   K   |  | 
|  |       |  | 
|  |       |  | 
|  |      {icon}|  | 
|   -------   | 
|           {icon}K| 
 -------------  
 ''',
 f''' 
  { 'Hidden' }
  -------------
 | * * * * * * |
 |* * * * * * *|
 | * * * * * * |
 |* * * * * * *|
 | * * * * * * |
 |* * * * * * *|
 | * * * * * * |
 |* * * * * * *|
 | * * * * * * |
 |* * * * * * *|
 |* * * * * * *|
  -------------'''
]
    if (game == "y"):
        rand1 = random.randrange(0,13)
        rand2 = random.randrange(0,13)
        print ("Player's Card: ")
        card_1 = Cards_art[rand1].strip().splitlines()
        card_2 = Cards_art[rand2].strip().splitlines()
        # Print side-by-side
        for card1, card2 in zip(card_1, card_2):
            print(f"{card1} {card2}")
        player_score += cards[rand1]+cards[rand2]
        
        print ("Computer's Card: ")
        rand1 = random.randrange(0,13)
        card_1 = Cards_art[rand1].strip().splitlines()
        card_2 = Cards_art[13].strip().splitlines()
        # Print side-by-side
        for card1, card2 in zip(card_1, card_2):
            print(f"{card1} {card2}")
        computer_score += cards[rand1]
        return player_score,computer_score
    
    elif (game == "hit"):
        rand = random.randrange(0,13)
        print ("Player's Card: ")
        card = Cards_art[rand].strip().splitlines()
        for iter in card:
            print(f"{iter}")
        if (player_score > 11 and rand == 0):
            player_score += 1
        else:
            player_score += cards[rand]
        
        rand = random.randrange(0,13)
        print ("Computer's Card: ")
        card = Cards_art[rand].strip().splitlines()
        for iter in card:
            print(f"{iter}")
        if (computer_score > 11 and rand == 0):
            computer_score += 1
        else:
            computer_score += cards[rand]
        return player_score,computer_score
        
    elif (game == "stand"):
        if (computer_score <= 17):
            rand = random.randrange(0,13)
            print ("Computer's Card: ")
            card = Cards_art[rand].strip().splitlines()
            for iter in card:
                print(f"{iter}")
            if (computer_score > 11 and rand == 0):
                computer_score += 1
            else:
                computer_score += cards[rand]     
        return player_score,computer_score
        
        
print ("Welcome to the BlackJack - Card Game.")
print ("Rules: Players compete against the Dealer(Computer) to get closer to 21 without going over.")

start = input("Press 'y' to Play and 'n' to Quit. ").lower()
if (start == "y"):
    print (" Let's Play! ")
    player_score,computer_score = draw_cards(start, 0,0)
    print (f"Player Score: {player_score}\t\t\tDealer Score: {computer_score}")
    
    while True:
        choice = input("Player will 'Hit' or 'Stand': ").lower()
        if (choice == "hit"):
            system_clean()
            player_score, computer_score = draw_cards(choice, player_score,computer_score)
            print (f"Player Score: {player_score}\t\t\tDealer Score: {computer_score}")
        elif (choice == "stand"):
            system_clean()
            player_score, computer_score = draw_cards(choice, player_score,computer_score)
            print (f"Player Score: {player_score}\t\t\tDealer Score: {computer_score}")
        
        if (computer_score > 11 and player_score > 11): 
            if (player_score <= 21 and (player_score > computer_score or computer_score > 21)):
                print ("Player Wins! ")
                break
            elif (player_score > 21):
                print ("Player Busted! Dealer Wins! ")
                break
            elif (player_score == computer_score):
                print ("It's a Draw! ")
                break
            elif (player_score < computer_score):
                print ("Dealer Wins! ")
                break