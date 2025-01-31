import smtplib
import datetime as dt
import random

email = "ommdevgoswami01@gmail.com"
password = "xozz sqdf dpvy lxqs"

now = dt.datetime.now()
day = now.weekday()
eList = ["ommdevgoswami@yahoo.com","swagatranjanbehera4@gmail.com","spandanbehera003@gmail.com"]

with open("AutoMail\\quotes.txt", "r") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)
    
    if day == 4:
        for i in eList:
            with smtplib.SMTP("smtp.gmail.com", port=587) as quoteSender:
                quoteSender.starttls()
                quoteSender.login(user=email, password=password)
                quoteSender.sendmail(from_addr=email, 
                                    to_addrs=i,
                                    msg=f"Subject:Motivation Quotes for You\n\n{quote}"
                )