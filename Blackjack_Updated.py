import random
import os
from enum import Enum

LOGO = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                             |__/  
'''
class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def __repr__(self):
        return f"{self.rank}{self.suit.value}"
    
    def display(self):
        Cards_art = [
f'''
{ '      Ace        '   }
 -------------  
|A{self.suit.value}           | 
|   -------   | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|   -------   | 
|           {self.suit.value}A| 
 -------------  
 ''',   
 f'''
 { '      2        '   }
 -------------  
|2{self.suit.value}           | 
|   -------   | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|   -------   | 
|           {self.suit.value}2| 
 -------------  
 ''',  
f'''
{ '      3        '   }
 -------------  
|3{self.suit.value}           | 
|   -------   | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|   -------   | 
|           {self.suit.value}3| 
 -------------  
 ''', 
f'''
{ '      4        '   }
 -------------  
|4{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}4| 
 -------------  
 ''',  f'''
 { '      5        '   }
 -------------  
|5{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}5| 
 -------------  
 ''', 
 f'''
 { '      6        '   }
 -------------  
|6{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}6| 
 -------------  
 ''', 
  f'''
  { '      7        '   }
 -------------  
|7{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |       |  | 
|  |{self.suit.value}  {self.suit.value}  {self.suit.value}|  | 
|  |       |  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}7| 
 -------------  
 ''',
  f'''
  { '      8        '   }
 -------------  
|8{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |   {self.suit.value}   |  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |   {self.suit.value}   |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}8| 
 -------------  
 ''',
 f'''
 { '      9        '   }
 -------------  
|9{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |   {self.suit.value}   |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}9| 
 -------------  
 ''',  
 f'''
 { '      10        '   }
 -------------  
|10{self.suit.value}          | 
|   -------   | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |   {self.suit.value}   |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |       |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|  |   {self.suit.value}   |  | 
|  |{self.suit.value}     {self.suit.value}|  | 
|   -------   | 
|          {self.suit.value}10| 
 -------------  
 ''',
 f'''
 { '     Jack       '   }
 -------------  
|J{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}      |  | 
|  |       |  | 
|  |       |  | 
|  |   J   |  | 
|  |       |  | 
|  |       |  | 
|  |      {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}J| 
 -------------  
 ''',
 f'''
 { '    Queen      '   }
 -------------  
|Q{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}      |  | 
|  |       |  | 
|  |       |  | 
|  |   Q   |  | 
|  |       |  | 
|  |       |  | 
|  |      {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}Q| 
 -------------  
 ''',
 f'''
 { '     King       '   }
 -------------  
|K{self.suit.value}           | 
|   -------   | 
|  |{self.suit.value}      |  | 
|  |       |  | 
|  |       |  | 
|  |   K   |  | 
|  |       |  | 
|  |       |  | 
|  |      {self.suit.value}|  | 
|   -------   | 
|           {self.suit.value}K| 
 -------------  
 ''',
 f''' 
{ '    Hidden        '   }
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
        cardPosition = {
                        "A" : 0,
                        "2" : 1,
                        "3" : 2,
                        "4" : 3,
                        "5" : 4,
                        "6" : 5,
                        "7" : 6,
                        "8" : 7,
                        "9" : 8,
                        "10" : 9,
                        "J" : 10,
                        "Q" : 11,
                        "K" : 12,
                        "H" : 13}
        
        return Cards_art[cardPosition[self.rank]]
        

class Deck:
    def __init__(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 0]
        self.cards = [Card(suit, rank, value) for suit in Suit for rank, value in zip(ranks, values)]
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop() if self.cards else None

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "A":
            self.aces += 1
        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def display(self):
        card_lines = [card.display().split("\n") for card in self.cards]
        combined_lines = ["  ".join(line) for line in zip(*card_lines)]
        return "\n".join(combined_lines)

    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    
    def hit(self, deck):
        self.hand.add_card(deck.draw())
    
    def is_busted(self):
        return self.hand.value > 21

class BlackjackGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.dealer = Player("Dealer")
    
    def initial_deal(self):
        for _ in range(2):
            for player in self.players:
                player.hit(self.deck)
            self.dealer.hit(self.deck)
    
    def show_hands(self, reveal_dealer=False):
        for player in self.players:
            print(f"{player.name}:\n{player.hand.display()}\nTotal: {player.hand.value}\n")
        
        if reveal_dealer:
            print(f"Dealer:\n{self.dealer.hand.display()}\nTotal: {self.dealer.hand.value}\n")
        else:
            hidden_card = Card(Suit.HEARTS, "H", 0).display().split("\n")
            visible_card = self.dealer.hand.cards[0].display().split("\n")
            combined_dealer_hand = "\n".join("  ".join(line) for line in zip(visible_card, hidden_card))
            print(f"Dealer:\n{combined_dealer_hand}\n")

    
    def player_turn(self, player):
        while player.hand.value < 21:
            action = input(f"{player.name}, Hit or Stand? ").lower()
            if action == "hit":
                player.hit(self.deck)
                self.show_hands()
            else:
                break
    
    def dealer_turn(self):
        while self.dealer.hand.value < 17:
            self.dealer.hit(self.deck)
    
    def determine_winner(self):
        self.show_hands(reveal_dealer=True)
        for player in self.players:
            if player.is_busted():
                print(f"{player.name} busted! Dealer wins.")
            elif self.dealer.is_busted() or player.hand.value > self.dealer.hand.value:
                print(f"{player.name} wins!")
            elif player.hand.value < self.dealer.hand.value:
                print(f"Dealer wins against {player.name}!")
            else:
                print(f"{player.name} and Dealer push!")
    
    def play(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.initial_deal()
            self.show_hands()
            for player in self.players:
                self.player_turn(player)
            self.dealer_turn()
            self.determine_winner()
            loop = input("Press 'r' to restart or 'n' to Quit: ").lower()
            if loop == 'r':
                os.system("cls" if os.name == "nt" else "clear")
                self.__init__([player.name for player in self.players])
            else:
                print("Thanks for Playing!")
                break

def Game():
    os.system("cls" if os.name == "nt" else "clear")
    print(LOGO)        
    print ("Welcome to the BlackJack - Card Game.")
    print ("Rules: Players compete against the Dealer(Computer) to get closer to 21 without going over.")
    start = input("Press 'y' to Play and 'n' to Quit. ").lower()
    if (start == "y"):
        print ("Let's Play! ")
        names = input("Enter player names separated by commas: ").split(",")
        game = BlackjackGame([name.strip() for name in names])
        game.play()
        
Game()