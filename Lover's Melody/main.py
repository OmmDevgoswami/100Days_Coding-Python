import smtplib
import random 
import datetime as dt
import json

MY_MAIL = "	rizzingyouheart@gmail.com"
MY_PASSWORD = "mirc yvzb ktey xgll"
RECIEVER_ADD = ["ritusnehanayak@gmail.com", "ommdevgoswami01@gmail.com", "ommdevgoswami@yahoo.com"]

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
    message = ""
    with open(finalLetter, "r", encoding='utf-8') as poem:
        content = poem.readlines()
        subject = content[0].strip()  
        message = "".join(content[1:])   
        # print(message)
    
    for email in RECIEVER_ADD:
        with smtplib.SMTP("smtp.gmail.com", port=587) as loveMelody:
            loveMelody.starttls()
            loveMelody.login(user=MY_MAIL, password=MY_PASSWORD)
            loveMelody.sendmail(from_addr=MY_MAIL,
                                to_addrs=email,
                                msg=f"Subject: {subject}\n\n{message}")
    print("Successfully Sent")
    
else:
    for email in RECIEVER_ADD:
        with smtplib.SMTP("smtp.gmail.com", port=587) as loveMelody:
            loveMelody.starttls()
            loveMelody.login(user=MY_MAIL, password=MY_PASSWORD)
            loveMelody.sendmail(from_addr=MY_MAIL,
                                to_addrs=email,
                                msg=f"Subject: Words of Heart\n\nI Love You")
    print("Successfully Sent")