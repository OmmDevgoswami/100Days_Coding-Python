import smtplib
import random 
import datetime as dt
import json

MY_MAIL = "	rizzingyouheart@gmail.com"
MY_PASSWORD = "gphc zikf flle xbf"
RECIEVER_ADD = ["ommdevgoswami01@gmail.com", "ommdevgoswami@yahoo.com"]

LETTERS_FILE = "Lover's Melody\\letters.json"
with open(LETTERS_FILE, "r", encoding="utf-8") as file:
        letters = json.load(file)
        
# letters = ["Message1.txt", "Message2.txt", "Message3.txt", "Message4.txt", "Message5.txt",
#            "Message6.txt", "Message7.txt", "Message8.txt", "Message9.txt", "Message10.txt"]

format = "Lover's Melody\\Poetic Mastry\\"
sent = []

if letters:
    letterChoice = random.choice(letters)
    sent.append(letterChoice)
    letters.remove(letterChoice)
    
    with open(LETTERS_FILE, "w", encoding="utf-8") as file:
        json.dump(letters, file)
    
    finalLetter = format + letterChoice
    with open(finalLetter, "r", encoding='utf-8') as poem:
        content = poem.readlines()
        print(content)

    print("Remaining letters:", letters)
    print("Sent letters:", sent)
    
    
    
else:
    print("No letters available")